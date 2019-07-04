from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView




class LoginView(TemplateView):

  template_name = 'Back_office/loginBO.html'

  def post(self, request, **kwargs):

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.medecin_type == 'Admin':
        login(request, user)
        return HttpResponseRedirect( reverse('dashboard') )

    return render(request, self.template_name)


class LogoutView(TemplateView):

  template_name = 'Back_office/loginBO.html'

  def get(self, request, **kwargs):

    logout(request)

    return render(request, self.template_name)



def dashboard(request):
    return render(request, './Back_office/index.html')