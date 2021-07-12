from django.contrib.auth import login, authenticate
# from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm, LoginForm
from accounts.models import User


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            nickname = form.cleaned_data.get('nickname')
            account = User.objects.create_user(
                email=email,
                password=password,
                nickname=nickname
            )
            account.save()

            return redirect('accounts:login')

    return render(request, 'signup.html')

# 구현한 거 : 등록된 유저가 없는경우, 비밀번호 틀린 경우 다르게 alert
def loginUser(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            User.objects.get(email=email)
        except:
            context = {
                'alert_flag': True, 'message': "등록된 email이 아닙니다."
            }
            return render(request, 'login.html', context)
        print('과연rew')
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('board:index')
        else:
            context = {
                'alert_flag': True, 'email': email, 'message': "비밀번호가 일치하지 않습니다."
            }
            return render(request, 'login.html', context)
    return render(request, 'login.html')


def profile(request, uid):
    print(uid)
    return render(request, 'profile.html', {'uid': uid})


def modify_nickname(request, uid):
    if request.method == 'POST':
        user = User.objects.get(pk=uid)
        user.nickname = request.POST['nickname']
        user.save()
        return redirect('accounts:profile', uid)

    return render(request, 'modify_nickname.html', {'uid': uid})


def delete_user(request, uid):
    if request.method == 'POST':
        user = User.objects.get(pk=uid)
        cur_password = request.POST['password']
        if user.check_password(cur_password):
            user.delete()
            return redirect('board:index')
        return render(request, 'delete_user.html', {'alert_flag': True, 'uid': uid})
    return render(request, 'delete_user.html', {'uid': uid})


# todo : 메일로 비밀번호 초기화 시키기
def modify_password(request, uid):
    if request.method == 'POST':
        user = User.objects.get(pk=uid)
        cur_password = request.POST['password']
        print(user.check_password(cur_password))
        return redirect('accounts:profile', uid)
    return render(request, 'modify_password.html', {'uid': uid})
