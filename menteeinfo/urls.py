from django.contrib import admin
from django.urls import path, include
from menteeinfo import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('registration/', views.register), 
    # path('registration/regcom/', views.menteereg),  
    path('sarc_ka_naya_logo_achha_hai', views.export, name="export"),  
    # path('upload/', views.simple_upload) 
    path('savedata_new', views.thank, name='savedata_new'),
    path('api/thanks', views.testapi, name="testapio"), 
    path('phonehome', views.phonehome, name='phonehome'), 
]