import django
import django.contrib.auth.views as auth_views
from django.urls import path, re_path

from .views import SignUpView

urlpatterns=[
    path('signup/',SignUpView.as_view(),name='signup'),
    re_path(r'^logout/$',auth_views.LogoutView.as_view(),name="logout")
]