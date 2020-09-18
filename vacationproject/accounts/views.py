from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        #예외상황
        if request.POST['password1'] == request.POST['password2']: #password1은 첫번째로 입력한 비번 같은지 확인을 위한 password2는 2번째로 입력한 비번
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)#로그인을 하는 함수 import해옴.
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':#로그인을 post로 request로 들어왔으니
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)#데이터베이스에서 실제로 있는 회원이 맞는지 확인(장고서버에 저장된 회원인지)
        if user is not None:#이미 존재하는 회원이라면 홈으로 감.
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error:' 'username or password is incorrect'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request) #로그아웃 함수 실행
        return redirect('home')
    return render(request, 'login.html')