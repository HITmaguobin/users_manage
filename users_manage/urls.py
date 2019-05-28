"""users_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include,path
from django.conf.urls import url
# from easyuitest import views
urlpatterns = [
    path('easyuitest/', include('easyuitest.urls')),
    path('admin/', admin.site.urls),
    # path('start/',views.app_start),
    # path('read/',views.read_all_sql),
    # path('edit/<id>',views.Edit_user),
    # path('remove/',views.Remove_user_id)
]
