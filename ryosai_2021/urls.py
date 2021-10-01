
from django.urls import path

from .views import Create , TwentysixView , Index
from . import views


urlpatterns = [
    
    path('',Index.as_view(), name="list"),
    
    path('create/',views.Create.as_view(), name="create"),
   
    path('1126/',TwentysixView.as_view(), name="1126"),
]