
from django.urls import path

from .views import IndexView, CreateView

urlpatterns = [
    path('',IndexView.as_view(), ),
    path('',CreateView.as_view(),)
]

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="list"),
    
   path('create/', views.Create.as_view(), name="create"),
]