from django.conf.urls import url

from usermanagement.views.login import LoginView, LogoutView

urlpatterns = [
    
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
