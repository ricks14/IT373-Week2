from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('announcement_list/', views.announcement_list, name='announcement_list'),
    path('announcement/<int:id>/', views.announcement, name='announcement'),
]