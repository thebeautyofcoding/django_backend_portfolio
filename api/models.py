from django.db import models

# Create your models here.


class Skill(models.Model):
    title = models.CharField(max_length=200)
    detailedDescription=models.TextField()
    shortDescription=models.CharField(max_length=300)
    
    
    def __str__(self):
        return self.title
    
    
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    detailedDescription=models.TextField()
    shortDescription=models.CharField(max_length=300)
    
    
    def __str__(self):
        return self.title
    

class Contact(models.Model):
    title=models.CharField(max_length=200)
    logoLink=models.CharField(max_length=300)
    description=models.CharField(max_length=300)