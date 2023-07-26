from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView

from apps.form import RegisterForm, CustomLoginForm


# class RegisterView(TemplateView):
#     template_name = 'index.html'
#     queryset = User.objects.all()\

def customur(request):
    return render(request,'customer.html')

def base(request):
    return render(request,'base.html')


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')

def Edit_profile(request):
    return render(request, 'Edit_profile.html')


class RegisterView(CreateView):
    template_name = 'index.html'
    queryset = User.objects.all()
    form_class = RegisterForm
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
        if not user or not user.is_active:
            return redirect('login')
        login(self.request, user)
        print(user)
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())



class CustomLoginView(FormView):
    form_class = CustomLoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], firs_name=form.cleaned_data['firs_name'], password=form.cleaned_data['password'])
        if not user or not user.is_active:
            return redirect('profile')
        login(self.request, user)
        print(user)
        return HttpResponseRedirect(self.get_success_url())