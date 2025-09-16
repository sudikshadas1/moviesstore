from django.urls import path
from . import views

app_name = 'movie_requests'
urlpatterns = [
    path('', views.requests_page, name='index'),
    path('<int:id>/delete/', views.delete_request, name='delete'),
]

