from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addTodo, name='add'),
    path('complete/<todo_id>/', views.completeTodo, name='complete'),
    path('deletecomplete/', views.deleteCompleted, name='deletecomplete'),
    path('deleteall/', views.deleteAll, name='deleteall'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('app/', views.app, name='app'),
    path('logout/', views.logoutUser, name='logout'),

]
