"""Bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('display', views.display),
    path('admin', views.admin),
    path('new',views.new),
    path('dele',views.dele),
    path('block',views.block),
    path('change',views.change),
    path('newpass',views.newpass),
    path('update',views.update),
    path('updatefinal',views.updatefinal),
    path('modify',views.modify),
    path('pay',views.pay),
    path('revert',views.revert),
    path('deltrans',views.deltrans),
]
