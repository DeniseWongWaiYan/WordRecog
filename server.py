from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor

class phoneconnect(Protocol):
    def connectionMade(self):
        print 'phone connected'

    def dataReceived(self, data):
        a = data.split(':')
        print a
        if len(a) > 1:
            command = a[0]
            content = a[1]

            msg=""
            if command == 'iam':
                self.name = content
                msg = self.name + 'has joined'

            elif command == 'message':
                msg = self.name + ':' + content
                print msg

            for client in self.factory.clients:
                client.message(msg)
                
    def message(self, message):
        self.transport.write(message + '\n')

        

factory = Factory()
factory.protocol = phoneconnect
reactor.listenTCP(80, factory)
print 'python ready'
reactor.run()
