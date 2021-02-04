from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# users accounts signup form.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("articles:list")
    else:
        form = UserCreationForm()
    content = {"form":form}
    return render(request, "accounts/signup.html", content)


# users accounts login form.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("articles:list")
    else:
        form = AuthenticationForm()
    content = {"form": form}
    return render(request, "accounts/login.html", content)


# logs out current user session.
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("accounts:log_in")
 