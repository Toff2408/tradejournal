from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Journal(models.Model):
    user = user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    date = models.DateField()
    pair = models.CharField(max_length=250)
    time_open = models.CharField(max_length=250)
    time_close = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)
    session = models.CharField(max_length=250)
    longorshort = models.BooleanField(default=True,null=True)
    entry = models.CharField(max_length=250,null=True)
    stop_loss = models.CharField(max_length=250,null=True)
    outcome = models.BooleanField(default=True,null=True)
    rr = models.DecimalField(max_digits=6, decimal_places=2)
    note = models.TextField(max_length=5000)

    def __str__(self):
        return self.pair
    

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)


    class Meta:
        db_table = 'profile'
        managed = True
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'