from django.db import models
from django.contrib.auth.models import User




class User(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.user.username


class Library(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Disease(models.Model):
    name = models.ForeignKey(Library,
                            on_delete= models.CASCADE)
    about = models.TextField()
    treatment = models.TextField()
    causes = models.TextField()
    symptoms = models.TextField()

    def __str__(self):
        return self.about

