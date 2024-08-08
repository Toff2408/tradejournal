from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('id','user','date','pair', 'time_open','time_close','duration','session','longorshort','entry','stop_loss','outcome','rr','note')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','first_name','last_name','email')