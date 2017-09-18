from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^users',  views.UsersView.as_view()),
    url(r'^user/me', views.UserView.as_view() ),
    url(r'^auth', views.AuthView.as_view() ),
    url(r'^locations', views.LocationsView.as_view() )
]
