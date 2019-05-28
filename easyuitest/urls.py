from django.urls import path
from .import views
app_name= 'easyuitest'

urlpatterns = [
    path('',views.app_start),
    path('login/',views.login),
    path('start/',views.app_start),
    path('read/',views.read_all_sql),
    path('edit/<id>',views.Edit_user),
    path('remove/',views.Remove_user_id),
    path('readurl/',views.read_all_sql_urlmanage),
    path('url_start/',views.url_start),
    path('edit_url/<id>',views.Edit_url),
    path('remove_url/',views.remove_url),
]
