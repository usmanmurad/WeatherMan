from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin

from Users.forms import RegisterForm


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'form': form, 'error': 'Cannot Register'})


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('profile')
        else:
            return render(request, 'login.html', {'error': 'Cannot Login'})


class ProfileView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'profile.html', {'user': request.user})


class LogoutView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request):
        logout(request)
        return redirect('login')
