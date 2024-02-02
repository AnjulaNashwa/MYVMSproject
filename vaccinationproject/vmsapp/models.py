from django.db import models
from django.contrib.auth.models import AbstractUser
# Inside your Python code

# Your code using Sheduleadd

# Create your models here.

class vaccination(AbstractUser):
    is_user=models.BooleanField(default=False)
    is_nurse=models.BooleanField(default=False)
    gender = models.CharField(max_length=300, null=True)
    childage= models.IntegerField(null=True,blank=True)
    childname= models.CharField(max_length=250)
    address= models.CharField(max_length=2000,null=True)
    name= models.CharField(max_length=250,null=True)
    hospital= models.CharField(max_length=2000,null=True)

class Hospital(models.Model):
    name = models.CharField(max_length=250,blank=True,null=True)
    place = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField()
    contact = models.CharField(max_length=250,blank=True,null=True)


    def __str__(self):
        return self.name or f"Hospital {self.name}"
class Vaccine(models.Model):
    vaccinename =models.CharField(max_length=250,blank=True,null=True)
    vaccinetype =models.CharField(max_length=20,blank=True,null=True)
    description =models.CharField(max_length=2000,blank=True,null=True)

    def __str__(self):
        return self.vaccinename or f"Vaccine {self.vaccinename}"

class Scheduleadd(models.Model):
    hospital =models.ForeignKey(Hospital,on_delete=models.DO_NOTHING)
    date =models.DateField()
    vaccinename =models.ForeignKey(Vaccine,on_delete=models.CASCADE)
    starttime =models.TimeField()
    endtime =models.TimeField()

class Complaint(models.Model):
    type = models.ForeignKey(vaccination,on_delete=models.DO_NOTHING)
    subject =models.CharField(max_length=250)
    complaints =models.CharField(max_length=250)
    date =models.DateField()
    reply =models.CharField(max_length=250,blank=True,null=True)

class Bookappointment(models.Model):
    user =models.ForeignKey(vaccination,on_delete=models.CASCADE)
    schedule =models.ForeignKey(Scheduleadd,on_delete=models.CASCADE)
    vaccinename= models.ForeignKey(Vaccine,on_delete=models.CASCADE)
    status =models.IntegerField(default=0)
    vaccinated=models.BooleanField(default=False)
    addreportcard =models.IntegerField(default=0)

class Vaccinationcard(models.Model):
    user =models.ForeignKey(vaccination,on_delete=models.DO_NOTHING)
    childage =models.IntegerField()
    vaccinename =models.CharField(max_length=250)
    date =models.DateField()
    addreportcard =models.IntegerField(default=0)
