
from django.urls import path

from .views import IndexView, CreateView , TwentysixView

from . import views


urlpatterns = [
    path('',IndexView.as_view(), ),
    path('',CreateView.as_view(),),

    path('', views.Index.as_view(), name="list"),
    
    path('create/', views.Create.as_view(), name="create"),
   
    path('1126/',TwentysixView.as_view(), name="1126"),
]