from django.db import models

class StudentModel(models.Model):
    idno =models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    email=models.EmailField(max_length=30,unique=True)
    password=models.CharField(max_length=8)
    photo =models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name

class JobDetails(models.Model):
    title = models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField(upload_to="jobimages/")

