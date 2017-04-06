//
//  ViewController.h
//  WordRecogios+Networking
//
//  Created by Denise Wong on 9/9/16.
//  Copyright © 2016 Denise Wong. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface ViewController : UIViewController <UIImagePickerControllerDelegate, UINavigationControllerDelegate>

@property (strong, nonatomic) IBOutlet UIImageView *imageView;

- (IBAction)takePhoto:(UIButton *)sender;

- (IBAction)choosePhoto:(UIButton *)sender;


@end

