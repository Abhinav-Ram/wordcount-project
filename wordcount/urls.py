from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name = 'home'),
    path('credits/',views.credits, name = 'credits'),
    path('app/', views.app, name = 'app'),
    path('count/', views.count, name = 'count'),
]
	