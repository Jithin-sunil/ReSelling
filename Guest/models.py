from django.db import models
from Admin.models import *
# Create your models here.
class tbl_user(models.Model):
    user_name = models.CharField(max_length=60)
    user_contact = models.CharField(max_length=60)
    user_email = models.CharField(max_length=60)
    user_password = models.CharField(max_length=60)
    user_address=models.CharField(max_length=60)
    user_place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    user_photo=models.FileField(upload_to="Assets/image/user")
    user_proof=models.FileField(upload_to="Assets/image/user")

class tbl_dealer(models.Model):
    dealer_place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    dealer_name = models.CharField(max_length=60)
    dealer_contact = models.CharField(max_length=60)
    dealer_email = models.CharField(max_length=60)
    dealer_password = models.CharField(max_length=60)
    license_no=models.CharField(max_length=60)
    establish_date= models.CharField(max_length=60)
    owner_name= models.CharField(max_length=60)
    owner_contact = models.CharField(max_length=60)
    owner_aadhar_no = models.CharField(max_length=60)
    owner_photo=models.FileField(upload_to="Assets/image/dealer")
    owner_proof=models.FileField(upload_to="Assets/image/dealer")
    license_proof=models.FileField(upload_to="Assets/image/dealer")
    dealer_logo=models.FileField(upload_to="Assets/image/dealer")
    dealer_address=models.CharField(max_length=60)
    dealer_status = models.IntegerField(default=0)

