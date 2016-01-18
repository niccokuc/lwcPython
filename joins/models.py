#This is the models code
from django.db import models

class Join(models.Model):
    name = models.TextField()
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add= True, auto_now=False)
    updated = models.DateTimeField(auto_now_add= False, auto_now=True)

    def __str__(self):
        return "Helloworld - This is djagngo 20"
        print("world is yours")