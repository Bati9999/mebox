from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    description = models.TextField()
    image=models.FileField()
    created_time=models.DateTimeField(auto_now_add=True)
    last_modified_time=models.DateTimeField(auto_now=True)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name
    
	
    
	