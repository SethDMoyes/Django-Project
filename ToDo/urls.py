#from django.urls import path
#from .views import ToDo_list

#urlpatterns = [
#    path('',ToDo_list)
#    ]

from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name="ToDo"
urlpatterns=[
        path('open', views.OpenView.as_view(), name='open'),
        path('', views.MainView.as_view(), name='all'),
        path('create/', views.ToDoCreateView.as_view(), name='ToDo_create'),
    ]