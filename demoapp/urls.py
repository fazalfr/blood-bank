from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="index"),
    path('register', views.register, name="register"),
    path('success', views.success, name="success"),
    path('login', views.login, name="login"),
    path('index', views.task,name="index"),
    path('add', views.add, name="add"),
    path('saved', views.saved, name="saved"),
    path('show', views.show, name="show"),
    path('show', views.logout, name='logout'),
    path('search', views.search, name="search"),
    path('result', views.result, name="result"),
    path('admin', views.admin, name="admin"),
    path('error', views.error, name="error"),
    path('edit', views.edit, name="edit"),
    path('delete', views.delete, name="delete"),
    path('deleted', views.deleted, name="deleted"),
    path('edited', views.edited, name="edited"),
    path('note', views.note, name="note"),
    path('profile', views.profile, name="profile"),
    path('message', views.message, name="message"),
    path('msges', views.msges, name="msges"),
    path('notification', views.notification, name="notification"),
    path('showmessage', views.showmessage, name="showmessage"),
    path('dltmsg', views.dltmsg, name="dltmsg"),

]
