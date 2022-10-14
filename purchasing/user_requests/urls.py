from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
app_name='user_requests'

urlpatterns = [
    url(r'^$',views.landing,name='landing'),
    url(r'^Request_form/$',views.form_view, name ="form"),
    url(r'^ty/$',views.thank_you,name='ty'),
    url(r'^ER_list$',views.ER_list,name='ER_list'),
    url(r'^accounts/login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    url(r'^accounts/logout/', auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    url(r'^accounts/profile/$', views.profile, name ='profile')
]


