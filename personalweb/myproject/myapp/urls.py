from django.urls import path
from myapp import views
urlpatterns =[
    path('',views.login),
    path('index',views.index)
]