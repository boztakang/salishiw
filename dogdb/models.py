from __future__ import unicode_literals

import datetime

from django.utils import timezone
from django.db import models

# Create your models here.
class Dog(models.Model):
    registered_name = models.CharField(max_length=200)
    call_name = models.CharField(max_length=200)
    registration_number = models.BigIntegerField()
    sex = models.CharField(max_length=1, choices= (("M", "Male"),("F","Female")) )
    date_of_birth = models.DateField('date of birth')
    picture = models.ImageField()
    
    def __str__(self):
        return self.registered_name
        

class NickNames(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nick_name
        
        
