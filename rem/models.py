from django.db import models
from django.urls import reverse
# Create your models here.

class rem(models.Model):
    rem_name = models .CharField(max_length=256,unique=True)
    rem_on = models.DateTimeField()

    def __str__(self):
        return self.rem_name
