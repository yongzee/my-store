from django.urls import path
from landingPage import views

urlpatterns = [
    path("", views.index, name='index'),
    path("features/", views.features, name='features'),
    path("about/", views.about, name='about'),
    path("comingsoon/", views.soon, name='soon'),
]