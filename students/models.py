from django.db import models

# Create your models here.
class students(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=20)

    def __str__(self) -> str:
        return super().__str__()