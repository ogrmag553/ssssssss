from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    create_at =models.DateTimeField(auto_now_add =True)  

    def __str__(self):
        return self.name 




class Autor(models.Model):
    name = models.CharField(max_length=50)
    biography = models. TimeField()
    birth_day = models.DateField(null=True)

    def __str__(self) -> str
       return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.DateField()
    isbh = models.CharField(max_length=12,unique=True)


Autor = models.ManyToManyField(Autor)

def __str__(self) -> str:
    return self.titele



