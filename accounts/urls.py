"""djangoecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import (
    register,
    index,
    update_user,
)

app_name = 'accounts'

urlpatterns = [
    path('', index, name='index'),

    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('sair/', LogoutView.as_view(), name='logout'),

    path('registrar/', register, name='register'),
    path('alterar-dados/', update_user, name='update_user'),
]