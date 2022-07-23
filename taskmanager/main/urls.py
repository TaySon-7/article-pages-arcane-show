from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about-us", views.about, name="about"),
    path("create", views.create, name="create"),
    path("article_page", views.test, name="articles"),
    path("about-us/Max Verstappen", views.Max, name="F1"),
    path("article_page/<slug:slug>", views.article_page, name="article_page")
]