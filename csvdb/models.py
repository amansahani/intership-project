from django.db import models

# Create your models here.
class CSVDB(models.Model):
    file = models.FileField(upload_to="files")