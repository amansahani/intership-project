from django.db import models

# Create your models here.

class Books(models.Model):
    isbn = models.IntegerField(null=True)
    title = models.CharField(max_length=400)
    author = models.CharField(max_length=400)
    publisher = models.CharField(max_length=200)
    img_urls = models.CharField(max_length=400)

    def __str__(self):
        return self.name

