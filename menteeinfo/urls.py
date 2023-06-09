from django.contrib import admin
from django.urls import path, include
from menteeinfo import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('registration/', views.register), 
    # path('registration/regcom/', views.menteereg),  
    path('2023_k_webCTM_achhe_hain', views.export, name="export"),  
    # path('upload/', views.simple_upload) 
    path('mentorReg', views.mentorReg, name='mentorReg'),
    # path('api/thanks', views.testapi, name="testapio"), 
    path('phonehome', views.phonehome, name='phonehome'),
]