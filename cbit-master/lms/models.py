from django.db import models


# Create your models here.


class Courses(models.Model):
    
    semister = models.CharField(max_length=5)
    branch=models.CharField(max_length=5)
    sub1 = models.CharField(max_length=200)
    sub2 = models.CharField(max_length=200)
    sub3 = models.CharField(max_length=200)
    sub4 = models.CharField(max_length=200)


    def __str__(self):
        return self.semister

class Course_details(models.Model):
    subject = models.CharField(max_length=200)
    topic1 = models.CharField(max_length=200)
    topic2 = models.CharField(max_length=200)
    topic3 = models.CharField(max_length=200)
    topic4 = models.CharField(max_length=200)
    
    def __str__(self):
        return self.subject
class stud_details(models.Model):
    semister = models.CharField(max_length=5)
    branch=models.CharField(max_length=5)
    username=models.CharField(primary_key=True,max_length=200)

    def __str__(self):
        return self.username
class lecture_files(models.Model):
    sub_topic= models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    lecture_vedios = models.FileField(upload_to='tutorial/attachments/',null=True)
    lecture_notes = models.FileField(upload_to='tutorial/notes/',null=True)
    
    def __str__(self):
        return self.sub_topic
    def delete(self, *args, **kwargs):
        self.feature_image.delete()
        self.attachment.delete()
        super().delete(*args, **kwargs)



