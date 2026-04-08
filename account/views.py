# Django imports for authentication and forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django import forms
from django.contrib.auth.models import User
from user.models import Profile


# Custom registration form extending Django's UserCreationForm
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)
    phone_number = forms.CharField(required=False, max_length=20)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "phone_number",
        )

    def save(self, commit=True):
        # Save the user and create a related Profile
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                first_name=self.cleaned_data["first_name"],
                last_name=self.cleaned_data["last_name"],
                phone_number=self.cleaned_data["phone_number"],
            )
        return user


# Handle user registration
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in user after registration
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "signup.html", {"form": form})


# Handle user logout
def log_out(request):
    logout(request)
    return redirect("/")


# Handle user sign in
def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log in user after authentication
            return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, "signin.html", {"form": form})
