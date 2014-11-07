from django.db import models

# Create your models here.

class BookCatalog(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image=models.FileField()
    
    def __str__(self):             
        return self.name

  
  
class BookTag(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
        
    def __str__(self):              
        return self.name
        

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    description = models.TextField()
    saler=models.CharField(max_length=200,blank=True)
    buy_link= models.CharField(max_length=200,blank=True)
    image=models.FileField()
    created_time=models.DateTimeField(auto_now_add=True)
    last_modified_time=models.DateTimeField(auto_now=True)
    catalog=models.ForeignKey(BookCatalog)
    tags = models.ManyToManyField(BookTag)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name
    
	
    



      
        
    
	