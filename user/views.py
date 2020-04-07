from django.shortcuts import render, redirect

# Pre-def form from django
# from django.contrib.auth.forms import UserCreationForm

# this is my custom form
import user
from .forms import Custom_User_Form, User_Update_Form, Profile_Update_Form

# for routing restrictions(user can access certain pages only when he logged in
# @ login_required (Manual)
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.contrib.auth.models import User


# Create your views here.
def register(request):
    #  POST request for posting the values
    if request.method == 'POST':

        # form = UserCreationForm(request.POST)
        form = Custom_User_Form(request.POST)
        if form.is_valid():
            form.save()
            # for getting values from the form
            username = form.cleaned_data.get('username')
            print("Account is Created for ", username)
            return redirect('blog-home')

    # GET is for only viewing the form
    else:
        # form = UserCreationForm()
        form = Custom_User_Form()
    return render(request, template_name='user/Register_form.html', context={'form': form})


@login_required
def profile(request):
    # to check whether the request is POST  and checking if data is valid
    if request.method == 'POST':
        # to show the textField with current data
        user_update_form = User_Update_Form(request.POST, instance=request.user)
        profile_update_form = Profile_Update_Form(request.POST, request.FILES, instance=request.user.profile)

        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, f'Your account has been Updated...')
            return redirect('user-profile')

    else:
        user_update_form = User_Update_Form(instance=request.user)
        profile_update_form = Profile_Update_Form(instance=request.user.profile)

    context = {
        'u_form': user_update_form,
        'p_form': profile_update_form
    }

    return render(request, template_name='user/profile.html', context=context)
