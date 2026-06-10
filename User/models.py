from django.db import models
from Admin.models import *
from Guest.models import *
from Dealer.models import *

class tbl_booking(models.Model):
    booking_date=models.DateField(auto_now_add=True)
    booking_status= models.IntegerField(default=0)
    booking_amount= models.IntegerField(default=0)
    vehicle_id=models.ForeignKey(tbl_vehicle,on_delete=models.CASCADE)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    user_review=models.CharField(max_length=500)
    vehicle=models.ForeignKey(tbl_vehicle,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)





class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=60)
    complaint_content=models.CharField(max_length=60)
    complaint_reply=models.CharField(max_length=60)
    complaint_status=models.IntegerField(default=0)
    complaint_date=models.DateField(auto_now_add=True)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_message(models.Model):
    message_title=models.CharField(max_length=60)
    message_content=models.CharField(max_length=60)
    message_reply=models.CharField(max_length=60)
    message_status=models.IntegerField(default=0)
    message_date=models.DateField(auto_now_add=True)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    vehicle_id=models.ForeignKey(tbl_vehicle,on_delete=models.CASCADE)



class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=60)
    feedback_date=models.DateField(auto_now_add=True)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

