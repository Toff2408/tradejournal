from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('dashboard',dashboard,name='dashboard'),
    path('journal',journal,name='journal'),
    path('userlogin',userlogin,name='userlogin'),
    path('signout',signout,name='signout'),
    path('signup',signup,name='signup'),
    path('learnforex',learnforex,name='learnforex'),
    path('profile',profile,name='profile'),
    path('journal/update/<int:journal_id>',update,name='update'),
]