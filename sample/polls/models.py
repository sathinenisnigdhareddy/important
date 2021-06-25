from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
   smcmenber = models.BooleanField(default=True,null=True)
# Create your models here.
class lecture_files(models.Model):
    sub_topic= models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    lecture_vedios = models.FileField(upload_to='attachments/',null=True)
    lecture_notes = models.FileField(upload_to='notes/',null=True)
    
    def __str__(self):
        return self.sub_topic
