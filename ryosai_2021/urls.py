
from django.urls import path

from .views import  Create , TwentysixView , Index ,TwentyfourView ,TwentyfiveView,TwentyeightView, TwentynineView ,TwentysevenView,ThirtyView,ThirtyoneView
from . import  views


urlpatterns = [
    
    path('',Index.as_view(), name="list"),
    
    path('create/',views.Create.as_view(), name="create"),
   
    path('1126/',TwentysixView.as_view(), name="column"),
    
    path('1127/',TwentysevenView.as_view(), name="2019"),
    
    path('1128/',TwentyeightView.as_view(), name="2020"),
    
    path('1129/',TwentynineView.as_view(), name="2021"),
    
     path('1130/',ThirtyView.as_view(), name="column"),
     
     path('1131/',ThirtyoneView.as_view(), name="column"),
     
     path('1125/',TwentyfiveView.as_view(), name="column"),
     
      path('1124/',TwentyfourView.as_view(), name="column")
    
    
]