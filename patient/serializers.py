from  rest_framework import serializers
from .models import Patient



class PatientSerializer(serializers.Serializer):
     patient_name = serializers.CharField(max_length=50) 
     Patient_emailid= serializers.EmailField()

  