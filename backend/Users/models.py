from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    create_at =models.DateTimeField(auto_now_add =True)  

    def __str__(self):
        return self.name 

