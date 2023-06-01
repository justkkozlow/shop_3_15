from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required

from apps.accounts.forms import RegisterForm, UserForgotPasswordForm, UserSetNewPasswordForm
from apps.accounts.models import Order


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "accounts/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class RegisterFormView(FormView):
    form_class = RegisterForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/registration.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ForgotPasswordFormView(FormView):
    form_class = UserForgotPasswordForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/forgot_pass.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def a_change_password(request):
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = UserSetNewPasswordForm(request.POST)
        if form.is_valid():
            old_password = request.POST.get("old_password")
            new_pass = request.POST.get("new_password")
            new_pass_rep = request.POST.get("new_password_repeat")
            form.save()
            return redirect('/login')

    else:
            form = UserSetNewPasswordForm(user)

    return render(request, 'accounts/login.html',
              {'form': form, 'user': user})


@login_required
def dashboard(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    return render(request, 'accounts/dashboard.html', {'orders': orders})
