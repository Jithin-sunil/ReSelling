from django.db import models


# Create your models here.

class tbl_district(models.Model):
    district_name = models.CharField(max_length=60)

class tbl_admin(models.Model):
    admin_name = models.CharField(max_length=60)
    admin_contact = models.CharField(max_length=60)
    admin_email = models.CharField(max_length=60)
    admin_password = models.CharField(max_length=60)



class tbl_modelyear(models.Model):
    modelyear_value= models.IntegerField(null=True)

class tbl_bodytype(models.Model):
    bodytype_name = models.CharField(max_length=60)

class tbl_company(models.Model):
    company_name = models.CharField(max_length=60)

class tbl_model(models.Model):
    model_name = models.CharField(max_length=60)
    company=models.ForeignKey(tbl_company,on_delete=models.CASCADE,null=True)

class tbl_seatingcapacity(models.Model):
    seatingcapacity_value= models.CharField(max_length=60)


class tbl_doorcount(models.Model):
    doorcount_value = models.CharField(max_length=60)

class tbl_fueltype(models.Model):
    fueltype_name= models.CharField(max_length=60)


class tbl_engineconfiguration(models.Model):
    engineconfiguration_value= models.CharField(max_length=60)


class tbl_transmissiontype(models.Model):
    transmissiontype_name = models.CharField(max_length=60)

class tbl_drivetrain(models.Model):
    drivetrain_type = models.CharField(max_length=60)

class tbl_ownershipcount(models.Model):
    OwnershipCount_type = models.CharField(max_length=60)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=60)
    pincode_value=models.CharField(max_length=60)
    district_name=models.ForeignKey(tbl_district,on_delete=models.CASCADE)



    
    


