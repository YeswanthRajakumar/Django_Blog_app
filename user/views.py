from django.shortcuts import render, redirect

# Pre-def form from django
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    #  POST request for posting the values
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # for getting values from the form
            username = form.cleaned_data.get('username')
            print("Account is Created for ", username)
            return redirect('blog-home')

    # GET is for only viewing the form
    else:
        form = UserCreationForm()
    return render(request, template_name='user/Register_form.html', context={'form': form})
