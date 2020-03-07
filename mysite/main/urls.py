from django.conf.urls import url

from main.views.login import LoginView, LogoutView
from main.views.registration import SignupView

urlpatterns = [
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
