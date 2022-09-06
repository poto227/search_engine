"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
#include 는 찾은 url패턴에 대해 다른 urls파일로 넘겨주는 역할 - accounts라는 단어가 있는 url을 만나면 include를 통해 users App의 urls 파일로 넘겨준다

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), #include를 통해 accounts/urls.py 사용 가능
    # path('product/', include('product.urls')),
    # path('order/', include('order.urls')),
]
