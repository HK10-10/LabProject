from django.db import models
from lab.models import Lab

class Patient(models.Model):
    registered_lab_name = models.CharField(max_length=50)
    patient_name = models.CharField(max_length=50)
    Patient_emailid = models.CharField(max_length=50)
    user_password = models.CharField(max_length=10)
    Test_name = models.CharField(max_length=50)
    Patient_dob= models.IntegerField()
    Aadharno = models.IntegerField()

    lab= models.ForeignKey(Lab,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

   

