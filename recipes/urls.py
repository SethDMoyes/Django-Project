from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name="recipes"
urlpatterns=[
        path('open', views.OpenView.as_view(), name='open'),
        path('', views.MainView.as_view(), name='all'),
        path('create/', views.RecipeCreateView.as_view(), name='recipes_create'),
    ]