from django.db import models

class Counter_app(models.Model):

    number =  models.IntegerField(default=0)
    
