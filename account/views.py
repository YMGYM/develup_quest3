from django.shortcuts import render, redirect
# 로그인 구현을 위한 auth
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.user.is_authenticated:
        # 로그인이 안되어있는 상태에서만 진입 가능
        return redirect('account:loginchk')
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(username=request.POST["username"],password=request.POST["password1"],email=request.POST["email"])
            auth.login(request, user)
            return redirect('account:loginchk')
        return render(request, 'signup.html',{'error':'비밀번호가 같지 않습니다.'})
    
    return render(request, 'signup.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect('account:loginchk')
    
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('account:loginchk')
        else:
            return render(request, 'signin.html', {'error': '아이디나 비밀번호를 다시 확인해주세요'})
        
        
    return render(request, 'signin.html')

@login_required(login_url='account:signin')
def signout(request):
    auth.logout(request)
    return redirect('account:loginchk')


def loginchk(request):
    
    return render(request, 'chk.html')


@login_required(login_url='account:signin')
def edituser(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password1"]
        user = auth.authenticate(username=username, password=request.POST["old_password"])
        if user is not None:
            if password == request.POST["password2"]:
                edit_user = User.objects.get(username=username)
                edit_user.set_password(password)
                edit_user.save()
                
                auth.login(request, edit_user)
                return redirect('account:loginchk')
            else:
                return render(request, 'edituser.html', {'error': '비밀번호가 일치하지 않습니다.'})
        else:
            return render(request, 'edituser.html', {'error': '사용자가 확인되지 않습니다.'})
        
        
    return render(request, 'edituser.html')


@login_required(login_url='account:signin')
def loginonly(request):
    return render(request, 'login_only.html')


def mainpage(request):
    return render(request, 'main.html')