from django.shortcuts import render , redirect
from .forms import UserForm,NewUserForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('/products')

    else:
        user_form = UserForm()

    context = {'user_form' : user_form}

    return render(request , 'registration/register.html' , context)

from django.contrib.auth import login
from django.contrib import messages

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})

@login_required
def profile(request):
    return render(request ,'registration/profile.html')

# def password_reset_done(request):
#     return render(request ,'registration/password_reset_done.html')
