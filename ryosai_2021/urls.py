
from django.urls import path

from .views import  Create , TwentysixView , Index , TwentyeightView, TwentynineView ,TwentysevenView
from . import  views


urlpatterns = [
    
    path('',Index.as_view(), name="list"),
    
    path('create/',views.Create.as_view(), name="create"),
   
    path('1126/',TwentysixView.as_view(), name="1126"),
    
    path('1127/',TwentysevenView.as_view(), name="1127"),
    
    path('1128/',TwentyeightView.as_view(), name="1128"),
    
    path('1129/',TwentynineView.as_view(), name="1129"),
    
    
]