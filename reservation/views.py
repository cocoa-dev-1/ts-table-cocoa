import django
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, get_user_model, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.regex_helper import contains
from users.models import MyUser as User
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView,
    PasswordChangeView, PasswordChangeDoneView
)
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
    PasswordChangeForm
)
from .models import Reservation
from TStable.settings import TIME_ZONE
import datetime
from pytz import timezone

# Create your views here.

identity_list = {
    '선생님': '선생님',
    '학생':'학생',
    '일반인':'일반인'
}

def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['password']

        user = authenticate(email=email, password=pwd)

        if user is not None:
            django_login(request, user)
            return redirect(profile)
        else:
            return render(request, 'user/login.html', context={
                'error': '로그인 정보가 일치하지 않아 로그인에 실패하엿습니다. 다시 시도해 주세요.'
            })

def logout(request):
    django_logout(request)
    return redirect(login)
        

def register(request):
    if request.method == 'GET':
        context = {'identity_list': identity_list}
        return render(request, 'user/register.html', context)
    elif request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['password']
        real_name = request.POST['real-name']
        identity = request.POST['identity']
        
        try:
            user = User.objects.create_user(email, real_name, identity, pwd)
            user.save()
            return redirect(login)
        except IntegrityError as e:
            context = {
                'identity_list': identity_list,
                'error': '다른 사람과 중복된 이메일 입니다.'
            }
            return render(request, 'user/register.html', context)

@login_required(login_url=login)
def profile(request):
    """
        TODO:
        1. 프로필 화면에 띄울 예약 현황 렌더링 로직
    """
    if request.method == 'GET':
        user_model = User.objects.get(email=request.user.email)
        reservation_model = list(Reservation.objects.filter(user = user_model.id))
        for i in reservation_model:
            if i.end_time > datetime.datetime.now(timezone('Asia/Seoul')):
                i.type = '예약'
            else:
                i.type = '종료'
            print(i)

        return render(request, 'profile/base.html', context={
            'reservation':reservation_model
        })


class UserPasswordResetView(PasswordResetView):
    template_name = 'user/password_reset.html' #템플릿을 변경하려면 이와같은 형식으로 입력
    success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm
    
    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exists():
            return super().form_valid(form)
        else:
            return render(self.request, 'user/password_reset_done_fail.html')
            
class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'user/password_reset_done.html' #템플릿을 변경하려면 이와같은 형식으로 입력

class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'user/password_reset_confirm.html'

class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'user/password_reset_complete.html'

class UserPasswordChangeView(PasswordChangeView):
    template_name = 'user/password_change_form.html'
    form_class = PasswordChangeForm

    def form_valid(self, form):
        if self.request.user.check_password(self.request.POST.get("old_password")):
            return super().form_valid(form)
        else:
            return render(self.request, 'user/password_change_done_fail.html')

class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'user/password_change_done.html'
    
    