from django.db import models
class Lab(models.Model):
    lab_id = models.AutoField
    lab_name= models.CharField(max_length=50)
    lab_emailid= models.CharField(max_length=50)
    lab_mobno= models.IntegerField()
    user_password= models.CharField(max_length=10)

 
