from django.db import models

# Create your models here.
class Offering(models.Model):
    title = models.CharField(max_length=200)
    short_desc = models.TextField()
    long_desc = models.TextField()
    

    def __str__(self):
        return self.title

