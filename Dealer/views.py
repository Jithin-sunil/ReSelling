from django.shortcuts import render,redirect
from Admin.models import *
from Dealer.models import *
from Guest.models import *
from User.models import *

from decimal import Decimal
from django.http import JsonResponse
import pickle
from datetime import datetime
import pandas as pd

# Create your views here.
def Homepage(request):
    if 'dlrid' not in request.session:
        return redirect('Guest:login')
    return render(request,'Dealer/Homepage.html')


def VehicleRegistration(request):
    if 'dlrid' not in request.session:
        return redirect('Guest:login')
    companydata=tbl_company.objects.all()
    modeldata=tbl_model.objects.all()
    modelyeardata=tbl_modelyear.objects.all()
    bodytypedata=tbl_bodytype.objects.all()
    seatingcapacitydata=tbl_seatingcapacity.objects.all()
    doorcountdata=tbl_doorcount.objects.all()
    fueltypedata=tbl_fueltype.objects.all()
    engineconfdata=tbl_engineconfiguration.objects.all()
    transmissiondata=tbl_transmissiontype.objects.all()
    drivetraindata=tbl_drivetrain.objects.all()
    ownershipcountdata=tbl_ownershipcount.objects.all()
    dealer= tbl_dealer.objects.get(id=request.session['dlrid'])
    

    if request.method=='POST':
        regno=request.POST.get('txt_reg_no')
        vrc=request.FILES.get('img_RC')
        vinsurance=request.FILES.get('img_IC')
        vphoto=request.FILES.get('img_vehicle')
        vcmpny=tbl_company.objects.get(id=request.POST.get('sel_company'))
        vmodel=tbl_model.objects.get(id=request.POST.get('sel_model'))
        vmodelyear=tbl_modelyear.objects.get(id=request.POST.get('sel_modelyear'))
        vbodytype=tbl_bodytype.objects.get(id=request.POST.get('sel_Bodytype'))
        vseating=tbl_seatingcapacity.objects.get(id=request.POST.get('sel_Seatingcapacity'))
        doorcount=tbl_doorcount.objects.get(id=request.POST.get('sel_Doorcount'))
        fueltype=tbl_fueltype.objects.get(id=request.POST.get('sel_Fueltype'))
        enginecap=request.POST.get('txt_EngineCapacity')
        engineconf=tbl_engineconfiguration.objects.get(id=request.POST.get('sel_Engineconf'))
        power=request.POST.get('txt_power')
        torque=request.POST.get('txt_torque')
        transmissiontype=tbl_transmissiontype.objects.get(id=request.POST.get('sel_Transmission'))
        drivetrain=tbl_drivetrain.objects.get(id=request.POST.get('sel_Drivetrain'))
        ownercnt=tbl_ownershipcount.objects.get(id=request.POST.get('sel_Ownership'))
        Mielage=request.POST.get('txt_mielage')
        OdometerReading=request.POST.get('txt_odometerreading')
        price=request.POST.get('txt_VehiclePrice')

        tbl_vehicle.objects.create(registration_no=regno,vehicle_rc=vrc,vehicle_insurance=vinsurance,vehicle_photo=vphoto,vehicle_company=vcmpny,vehicle_model_name=vmodel,vehicle_model_year=vmodelyear,vehicle_bodytype=vbodytype,vehicle_seating_capacity=vseating,vehicle_door_count=doorcount,vehicle_fuel_type=fueltype,vehicle_engine_capacity=enginecap,vehicle_engine_configuration=engineconf,vehicle_power=power,vehicle_torque=torque,vehicle_transmission_type=transmissiontype,vehicle_drivetrain=drivetrain,vehicle_ownership_count=ownercnt,vehicle_mielage=Mielage,vehicle_odometer_reading=OdometerReading,dealer=dealer,vehicle_price=price)
        return render(request,'Dealer/VehicleRegistration.html',{'Company':companydata,'Model':modeldata,'Modelyear':modelyeardata,'Bodytype':bodytypedata,'Seatingcapacity':seatingcapacitydata,'Doorcount':doorcountdata,'Fueltype':fueltypedata,'Engineconf':engineconfdata,'Transmission':transmissiondata,'Drivetrain':drivetraindata,'Ownership':ownershipcountdata})
    else:
        return render(request,'Dealer/VehicleRegistration.html',{'Company':companydata,'Model':modeldata,'Modelyear':modelyeardata,'Bodytype':bodytypedata,'Seatingcapacity':seatingcapacitydata,'Doorcount':doorcountdata,'Fueltype':fueltypedata,'Engineconf':engineconfdata,'Transmission':transmissiondata,'Drivetrain':drivetraindata,'Ownership':ownershipcountdata})
       
def ChangePassword(request):
    if 'dlrid' not in request.session:
        return redirect('Guest:login')
    dealerpassData=tbl_dealer.objects.get(id=request.session['dlrid'])
    if request.method =="POST":
        db_pass=dealerpassData.dealer_password
        oldPassword=request.POST.get('txt_CurrentPassword')
        newPassword=request.POST.get('txt_NewPassword')
        confirmpass=request.POST.get('txt_ConfirmPassword')
        if db_pass == oldPassword:
            if newPassword == confirmpass:   
                dealerpassData.dealer_password=request.POST.get('txt_NewPassword')
                dealerpassData.save()
                return redirect('Dealer:DealerProfile')
            else:
                return render(request,'Dealer/ChangePassword.html',{'msg':" password  Mismatched"})
        else:
            return render(request,'Dealer/ChangePassword.html',{'msg':"Enter correct password"})
    return render(request,'Dealer/ChangePassword.html')

def DealerProfile(request):
    if 'dlrid' not in request.session:
        return redirect('Guest:login')
    dealerData=tbl_dealer.objects.get(id=request.session['dlrid'])
    return render(request,'Dealer/DealerProfile.html',{'dealerData':dealerData})

def EditProfile(request):
    if 'dlrid' not in request.session:
        return redirect('Guest:login')
    dealerpData=tbl_dealer.objects.get(id=request.session['dlrid'])
    if request.method =="POST":
        dealerpData.dealer_name=request.POST.get('txt_name')
        dealerpData.dealer_contact=request.POST.get('txt_contact')
        dealerpData.dealer_address=request.POST.get('txt_address')
        dealerpData.save()
        return redirect('Dealer:DealerProfile')
    return render(request,'Dealer/EditProfile.html',{'dealerpData':dealerpData})

def MyVehicles(request):
    if 'dlrid' not in request.session:
        return redirect('Guest:login')
    vehicledata=tbl_vehicle.objects.filter(dealer=request.session['dlrid'])
    return render(request,'Dealer/MyVehicles.html',{'vehicledata':vehicledata})
def delMyVehicles(request,did):
    if 'dlrid' not in request.session:
        return redirect('Guest:login')
    tbl_vehicle.objects.get(id=did).delete()
    return render(request,'Dealer/MyVehicles.html',{'msg':"deleted"})

def AddGallery(request,vid):
    if 'dlrid' not in request.session:
        return redirect('Guest:login')
    gallerydata=tbl_gallery.objects.filter(vehicle=vid)
    if request.method=='POST':
        photo=request.FILES.get('img_photo')
        vehicle=tbl_vehicle.objects.get(id=vid)
        tbl_gallery.objects.create(gallery_photo=photo,vehicle=vehicle)
        return render(request,'Dealer/AddGallery.html',{'gallerydata':gallerydata})
    else:
        return render(request,'Dealer/AddGallery.html',{'gallerydata':gallerydata})  
def delAddGallery(request,did):
    if 'dlrid' not in request.session:
        return redirect('Guest:login')
    tbl_gallery.objects.get(id=did).delete()
    return render(request,'Dealer/AddGallery.html',{'msg':"deleted"})

def ViewBooking(request):
    if 'dlrid' not in request.session:
        return redirect('Guest:login')
    bookdata=tbl_booking.objects.filter(vehicle_id__dealer=request.session['dlrid'])
    return render(request,'Dealer/ViewBooking.html',{'bookdata': bookdata})
def acptViewBooking(request,aid):
    if 'dlrid' not in request.session:
        return redirect('Guest:login')
    bookdata= tbl_booking.objects.get(id=aid)
    bookdata.booking_status=1
    bookdata.save()
    return render(request,'Dealer/ViewBooking.html',{'msg':"Accepted"})
def rejctViewBooking(request,rid):
    if 'dlrid' not in request.session:
        return redirect('Guest:login')
    bookdata= tbl_booking.objects.get(id=rid)
    bookdata.booking_status=2
    bookdata.save()
    return render(request,'Dealer/ViewBooking.html',{'msg':"Rejected"})

def UserDetails(request,uid):
    if 'dlrid' not in request.session:
        return redirect('Guest:login')
    userData=tbl_user.objects.get(id=uid)
    return render(request,'Dealer/UserDetails.html',{'userData':userData})

def ajaxmodel(request):
    model = tbl_model.objects.filter(company=request.GET.get('did'))
    return render(request, "Dealer/AjaxModel.html",{'model':model})

def logout(request):
    del request.session['dlrid']
    return redirect('Guest:Index')

def ViewMessages(request):
    if 'dlrid' not in request.session:
        return redirect('Guest:login')
    messagedata=tbl_message.objects.filter(message_status=0,vehicle_id__dealer=request.session['dlrid'])
    replydata=tbl_message.objects.filter(message_status=1,vehicle_id__dealer=request.session['dlrid'])
    return render(request,'Dealer/ViewMessages.html',{'messagedata':messagedata,'replydata':replydata})

def Reply(request,rid):
    if 'dlrid' not in request.session:
        return redirect('Guest:login')
    if request.method=="POST":
        reply=tbl_message.objects.get(id=rid)
        reply.message_reply=request.POST.get('txt_reply')
        reply.message_status=1
        reply.save()
        return redirect('Dealer:ViewMessages')
    return render(request,'Dealer/Reply.html')

#ml


model = pickle.load(open("Assets/Model/car_price_model.pkl","rb"))

brand_encoder = pickle.load(open("Assets/Model/brand_encoder.pkl","rb"))
model_encoder = pickle.load(open("Assets/Model/model_encoder.pkl","rb"))
trans_encoder = pickle.load(open("Assets/Model/trans_encoder.pkl","rb"))
owner_encoder = pickle.load(open("Assets/Model/owner_encoder.pkl","rb"))
fuel_encoder = pickle.load(open("Assets/Model/fuel_encoder.pkl","rb"))

def predict_car_price(request):
    companydata=tbl_company.objects.all()
    modeldata=tbl_model.objects.all()
    modelyeardata=tbl_modelyear.objects.all()
    price=None
    
    
    

    if request.method=="POST":

        modelobject=tbl_model.objects.get(id=request.POST.get("model"))
        model_name=modelobject.model_name
        brand=modelobject.company.company_name
        year = int(request.POST.get("sel_modelyear"))
        current_year = datetime.now().year
        age = current_year - year
        km=int(request.POST.get("km"))
        transmission=request.POST.get("sel_Transmission")
        owner=request.POST.get("owner")
        fuel=request.POST.get("fuel")

        brand=brand_encoder.transform([brand])[0]
        model_name=model_encoder.transform([model_name])[0]
        transmission=trans_encoder.transform([transmission])[0]
        owner=owner_encoder.transform([owner])[0]
        fuel=fuel_encoder.transform([fuel])[0]

        input_data=pd.DataFrame([[

            brand,
            model_name,
            age,
            km,
            transmission,
            owner,
            fuel

        ]],columns=['Brand','model','Age','kmDriven','Transmission','Owner','FuelType'])

        prediction=model.predict(input_data)

        price=" ₹ "+str(int(prediction[0]))

    return render(request,"Dealer/PricePrediction.html",{"price":price,'companydata':companydata,'Modelyear':modelyeardata})
