from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('allprojects', views.all_projects, name="all_projects"),
    path('contact',views.contact,name='contact'),
    path('categories/<slug:category_slug>',views.category_detail,name='projects_by_category'),
] 