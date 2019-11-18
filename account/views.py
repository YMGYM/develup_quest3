from django.shortcuts import render, redirect
# 로그인 구현을 위한 auth
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(username=request.POST["username"],password=request.POST["password1"])
            auth.login(request, user)
            return redirect('account:loginchk')
        return render(request, 'signup.html')
    
    return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # request.session['username'] = username
            return redirect('account:loginchk')
        else:
            return render(request, 'signin.html', {'error': '어디 내앞에서 감히 거짓말인가!'})
    return render(request, 'signin.html')


def signout(request):
    auth.logout(request)
    return redirect('account:loginchk')

def loginchk(request):
    
    return render(request, 'chk.html')

