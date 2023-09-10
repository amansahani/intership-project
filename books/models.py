from django.db import models

# Create your models here.

class Books(models.Model):
    isbn = models.CharField(max_length=100)
    title = models.CharField(max_length=400)
    author = models.CharField(max_length=400)
    year = models.CharField(max_length=10)
    publisher = models.CharField(max_length=200)
    img_url1 = models.CharField(max_length=400)
    img_url2 = models.CharField(max_length=400)
    img_url3 = models.CharField(max_length=400)

    def __str__(self):
        return self.name

