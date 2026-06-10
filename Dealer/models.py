from django.db import models
from Admin.models import *
from Guest.models import *

#Create your models here.
class tbl_vehicle(models.Model):
    registration_no = models.CharField(max_length=60,null=True)
    vehicle_rc=models.FileField(upload_to="Assets/image/product")
    vehicle_photo=models.FileField(upload_to="Assets/image/product")
    vehicle_insurance=models.FileField(upload_to="Assets/image/product")
    vehicle_company=models.ForeignKey(tbl_company,on_delete=models.CASCADE)
    vehicle_model_name=models.ForeignKey(tbl_model,on_delete=models.CASCADE)
    vehicle_model_year=models.ForeignKey(tbl_modelyear,on_delete=models.CASCADE)
    vehicle_bodytype=models.ForeignKey(tbl_bodytype,on_delete=models.CASCADE)
    vehicle_seating_capacity=models.ForeignKey(tbl_seatingcapacity,on_delete=models.CASCADE)
    vehicle_door_count=models.ForeignKey(tbl_doorcount,on_delete=models.CASCADE)
    vehicle_fuel_type=models.ForeignKey(tbl_fueltype,on_delete=models.CASCADE)
    vehicle_engine_capacity=models.CharField(max_length=60,null=True)
    vehicle_engine_configuration=models.ForeignKey(tbl_engineconfiguration,on_delete=models.CASCADE)
    vehicle_power=models.CharField(max_length=60)
    vehicle_torque=models.CharField(max_length=60)
    vehicle_transmission_type=models.ForeignKey(tbl_transmissiontype,on_delete=models.CASCADE)
    vehicle_drivetrain =models.ForeignKey(tbl_drivetrain,on_delete=models.CASCADE)
    vehicle_ownership_count=models.ForeignKey(tbl_ownershipcount,on_delete=models.CASCADE)
    vehicle_mielage=models.CharField(max_length=60)
    vehicle_odometer_reading=models.CharField(max_length=60)
    dealer = models.ForeignKey(tbl_dealer,on_delete=models.CASCADE,null=True)
    vehicle_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)

class tbl_gallery(models.Model):
    gallery_photo=models.FileField(upload_to="Assets/image/product")
    vehicle=models.ForeignKey(tbl_vehicle,on_delete=models.CASCADE)

