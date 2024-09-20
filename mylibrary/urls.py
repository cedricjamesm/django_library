from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-lib'),
    path('author-list/', views.author, name='auth-lib'),
    path('book-inst/<int:id>/', views.details, name='book-lib'),
]