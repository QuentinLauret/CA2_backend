# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):           #To create a form
    form_class = UserCreationForm               #To specify that we want to create a new user
    success_url = reverse_lazy("login")         #If the registration succeed, we redirect the user to the login page
    template_name = "registration/signup.html"  #The html page to show for the registration