from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login from .forms import LoginForm, UserRegistrationForm, UserEdit, ProfileEdit
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
from actions.utils import create_action
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from django.core.urlresolvers import reverse




# Create your views here.
def LoginView(request):

    if request.method =='POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active():
                    login(request, user)
                    return HttpResponse("Welcome aboard - suckers! I am Hexachlorophene J. Goodforttune, Kidnapper At-Large, and Devourer of Tortoises par Excellence, at your service.")

                else:
                    return HttpResponse("You're like the limit in this function. DNE!")
            else:
                return HttpResponse("If at first you don't succeed, try, try, try again. (Your login is invalid.)")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def UserRegistrationView(request):

    if request.method == 'POST':
        create_user_form = UserRegistrationForm(request.POST)

        if create_user_form.is_valid():
            new_user = create_user_form.save(commit=False)

            new_user.set_password(
                create_user_form.cleaned_data['password'])

            new_user.save()
            create_action(new_user, 'has created an account')
            profile = Profile.objects.create(user=new_user)

            return render(request, 'account/register_done.html', {'new_user': new_user})

    else:
        create_user_form = UserRegistrationForm()

    return render(request, 'account/register.html', {'create_user_form': create_user_form})


@login_required
def UserEditView(request):
    if request.method == 'POST':
        user_edit_form = UserEdit(instance=request.user, data=request.POST)
        profile_edit_form = ProfileEdit(instance=request.user.profile, data=request.POST, files=request.FILES)
                

        if user_edit_form.is_valid() and profile_edit_form.is_valid():
            user_edit_form.save()
            profile_edit_form.save()
            messages.success(request, 'Profile sucessfully edited.')

    else:
        user_edit_form = UserEdit(instance=request.user)
        profile_edit_form = ProfileEdit(instance=request.user.profile)
        messages.error(request, 'Whoops...there was an error updating your profile.')

    return render(request, 'account/edit.html', {'user_edit_form': user_edit_form, 'profile_edit_form': profile_edit_form} )


def handlephoto(request):
    
                              
