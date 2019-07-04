from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from backoffice import views
from backoffice.views import LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(), name='bo_login'),
    path('logout/', LogoutView.as_view(), name='bo_logout'),
    path('dashboard', login_required(views.dashboard), name='dashboard'),
]