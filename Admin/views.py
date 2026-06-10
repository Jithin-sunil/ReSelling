from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
# Create your views here.
def District(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    districtdata = tbl_district.objects.all()
    if request.method=='POST':
        district=request.POST.get('txt_district')
        tbl_district.objects.create(district_name=district)
        return render(request,'Admin/District.html',{'District':districtdata})
    else:
        return render(request,'Admin/District.html',{'District':districtdata})
def delDistrict(request,did):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    tbl_district.objects.get(id=did).delete()
    return redirect('Admin:District')
def edtDistrict(request,eid):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    districtdata = tbl_district.objects.get(id=eid)
    if request.method == "POST":
        districtdata.district_name = request.POST.get('txt_district')
        districtdata.save()
        return redirect('Admin:District')
    return render(request,'Admin/District.html',{'Districteditdata':districtdata})


    


def AdminRegistration(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    adminregistrationdata=tbl_admin.objects.all()
    if request.method=='POST':
        name=request.POST.get('txt_name')
        contact= request.POST.get('txt_contact')
        email =request.POST.get('txt_email')
        password=request.POST.get('txt_password')
        tbl_admin.objects.create(admin_name=name,admin_contact=contact,admin_email=email,admin_password=password)
        return render(request,'Admin/AdminRegistration.html',{'admin':adminregistrationdata})
    else:
        return render(request,'Admin/AdminRegistration.html',{'admin':adminregistrationdata})
def delAdminRegistration(request,did):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    tbl_admin.objects.get(id=did).delete()
    return redirect('Admin:AdminRegistration')
def edtAdminRegistration(request,eid):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    adminregistrationdata = tbl_admin.objects.get(id=eid)
    if request.method == "POST":
        adminregistrationdata.admin_name = request.POST.get('txt_name')
        adminregistrationdata.admin_contact = request.POST.get('txt_contact')
        adminregistrationdata.admin_email = request.POST.get('txt_email')
        adminregistrationdata.save()
        return redirect('Admin:AdminRegistration')
    return render(request,'Admin/AdminRegistration.html',{'AdminRegistrationeditdata':adminregistrationdata})


def Place(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    districtData=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    if request.method == 'POST':
        place=request.POST.get('txt_place')
        pin=request.POST.get('txt_pincode')
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(place_name=place,pincode_value=pin,district_name=district)
    return render(request,'Admin/Place.html',{'districtData':districtData,'placedata':placedata})
def delPlace(request,did):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    tbl_place.objects.get(id=did).delete()
    return redirect('Admin:Place')
def edtPlace(request,eid):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    districtData=tbl_district.objects.all()
    placedata = tbl_place.objects.get(id=eid)
    if request.method == "POST":
        placedata.district_name = tbl_district.objects.get(id=request.POST.get('sel_district'))
        placedata.place_name = request.POST.get('txt_place')
        placedata.pincode_value = request.POST.get('txt_pincode')
        placedata.save()
        return redirect('Admin:Place')
    return render(request,'Admin/Place.html',{'placeeditdata':placedata,'districtData':districtData})





def Product(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    return render(request,'Admin/Product.html')

def Homepage(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    adminData=tbl_admin.objects.get(id=request.session['aid'])
    dealercount=tbl_dealer.objects.count()
    usercount=tbl_user.objects.count()
    bookingData=tbl_booking.objects.all()
    return render(request,'Admin/Homepage.html',{'adminData':adminData,'dealercount':dealercount,'usercount':usercount,'bookingData':bookingData})



def ChangePassword(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    adminpassData=tbl_admin.objects.get(id=request.session['aid'])
    if request.method =="POST":
        db_pass=adminpassData.admin_password
        oldPassword=request.POST.get('txt_CurrentPassword')
        newPassword=request.POST.get('txt_NewPassword')
        confirmpass=request.POST.get('txt_ConfirmPassword')
        if db_pass == oldPassword:
            if newPassword == confirmpass:   
                adminpassData.admin_password=request.POST.get('txt_NewPassword')
                adminpassData.save()
                return redirect('Admin:Homepage')
            else:
                return render(request,'Admin/ChangePassword.html',{'msg':" password  Mismatched"})
        else:
            return render(request,'Admin/ChangePassword.html',{'msg':"Enter correct password"})
    return render(request,'Admin/ChangePassword.html')


def Company(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    companydata = tbl_company.objects.all()
    if request.method=='POST':
        company=request.POST.get('txt_Company')
        tbl_company.objects.create(company_name=company)
        return render(request,'Admin/Company.html',{'Company':companydata})
    else:
        return render(request,'Admin/Company.html',{'Company':companydata})
def delCompany(request,did):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    tbl_company.objects.get(id=did).delete()
    return redirect('Admin:Company')
def edtCompany(request,eid):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    compdata = tbl_company.objects.get(id=eid)
    if request.method == "POST":
        compdata.company_name = request.POST.get('txt_Company')
        compdata.save()
        return redirect('Admin:Company')
    return render(request,'Admin/Company.html',{'editdata':compdata})



def ModelName(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    modelnamedata=tbl_model.objects.all()
    companydata=tbl_company.objects.all()
    if request.method=='POST':
        modelname=request.POST.get('txt_ModelName')
        companyname=tbl_company.objects.get(id=request.POST.get('sel_company'))
        tbl_model.objects.create(model_name=modelname,company=companyname)
        return render(request,'Admin/ModelName.html',{'ModelName':modelnamedata,'companydata':companydata})
    else:
        return render(request,'Admin/ModelName.html',{'ModelName':modelnamedata,'companydata':companydata})
def delModelName(request,did):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    tbl_model.objects.get(id=did).delete()
    return redirect('Admin:ModelName')
def edtModelName(request,eid):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    companydata=tbl_company.objects.all()
    modelnamedata = tbl_model.objects.get(id=eid)
    if request.method == "POST":
        modelnamedata.model_name = request.POST.get('txt_ModelName')
        modelnamedata.company=tbl_company.objects.get(id=request.POST.get('sel_company'))
        modelnamedata.save()
        return redirect('Admin:ModelName')
    return render(request,'Admin/ModelName.html',{'modeleditdata':modelnamedata,'companydata':companydata})


def ModelYear(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    modelyeardata=tbl_modelyear.objects.all()
    if request.method=='POST':
        modelyear=request.POST.get('txt_ModelYear')
        tbl_modelyear.objects.create(modelyear_value=modelyear)
        return render(request,'Admin/ModelYear.html',{'ModelName':modelyeardata})
    else:
        return render(request,'Admin/ModelYear.html',{'ModelName':modelyeardata})
def delModelYear(request,did):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    tbl_modelyear.objects.get(id=did).delete()
    return redirect('Admin:ModelYear')
def edtModelYear(request,eid):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    modelyeardata = tbl_modelyear.objects.get(id=eid)
    if request.method == "POST":
        modelyeardata.modelyear_value = request.POST.get('txt_ModelYear')
        modelyeardata.save()
        return redirect('Admin:ModelYear')
    return render(request,'Admin/ModelYear.html',{'modelyeareditdata':modelyeardata})


def BodyType(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    bodytypedata=tbl_bodytype.objects.all()
    if request.method == "POST":
        bodytype=request.POST.get('txt_BodyType')
        tbl_bodytype.objects.create(bodytype_name=bodytype)
        return render(request,'Admin/BodyType.html',{'BodyType':bodytypedata})
    else:
        return render(request,'Admin/BodyType.html',{'BodyType':bodytypedata})
def delBodyType(request,did):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    tbl_bodytype.objects.get(id=did).delete()
    return redirect('Admin:BodyType')
def edtBodyType(request,eid):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    bodytypedata = tbl_modelyear.objects.get(id=eid)
    if request.method == "POST":
        bodytypedata.bodytype_name = request.POST.get('txt_BodyType')
        bodytypedata.save()
        return redirect('Admin:BodyType')
    return render(request,'Admin/BodyType.html',{'BodyTypeeditdata':bodytypedata})


def SeatingCapacity(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    seatingdata=tbl_seatingcapacity.objects.all()
    if request.method == "POST":
        seatingcapacity=request.POST.get('txt_SeatingCapacity')
        tbl_seatingcapacity.objects.create(seatingcapacity_value=seatingcapacity)
        return render(request,'Admin/SeatingCapacity.html',{'SeatingCapacity':seatingdata})
    else:
        return render(request,'Admin/SeatingCapacity.html',{'SeatingCapacity':seatingdata})
def delSeatingCapacity(request,did):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    tbl_seatingcapacity.objects.get(id=did).delete()
    return redirect('Admin:SeatingCapacity')
def edtSeatingCapacity(request,eid):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    seatingdata = tbl_seatingcapacity.objects.get(id=eid)
    if request.method == "POST":
        seatingdata.seatingcapacity_value = request.POST.get('txt_SeatingCapacity')
        seatingdata.save()
        return redirect('Admin:SeatingCapacity')
    return render(request,'Admin/SeatingCapacity.html',{'SeatingCapacityeditdata':seatingdata})


def DoorCount(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    doorcountdata=tbl_doorcount.objects.all()
    if request.method == "POST":
        doorcount=request.POST.get('txt_DoorCount')
        tbl_doorcount.objects.create(doorcount_value=doorcount)
        return render(request,'Admin/DoorCount.html',{'Doorcount':doorcountdata})
    else:
        return render(request,'Admin/DoorCount.html',{'Doorcount':doorcountdata})
def delDoorcount(request,did):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    tbl_doorcount.objects.get(id=did).delete()
    return redirect('Admin:DoorCount')
def edtDoorcount(request,eid):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    doorcountdata = tbl_doorcount.objects.get(id=eid)
    if request.method == "POST":
        doorcountdata.doorcount_value = request.POST.get('txt_DoorCount')
        doorcountdata.save()
        return redirect('Admin:DoorCount')
    return render(request,'Admin/DoorCount.html',{'DoorCounteditdata':doorcountdata})


def FuelType(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    fueltypedata=tbl_fueltype.objects.all()
    if request.method == "POST":
        fueltype=request.POST.get('txt_FuelType')
        tbl_fueltype.objects.create(fueltype_name=fueltype)
        return render(request,'Admin/FuelType.html',{'FuelType':fueltypedata})
    else:
        return render(request,'Admin/FuelType.html',{'FuelType':fueltypedata})
def delFuelType(request,did):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    tbl_fueltype.objects.get(id=did).delete()
    return redirect('Admin:FuelType')
def edtFuelType(request,eid):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    fueltypedata = tbl_fueltype.objects.get(id=eid)
    if request.method == "POST":
        fueltypedata.fueltype_name = request.POST.get('txt_FuelType')
        fueltypedata.save()
        return redirect('Admin:FuelType')
    return render(request,'Admin/FuelType.html',{'FuelTypeeditdata':fueltypedata})




def EngineConfiguration(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    engineconfdata=tbl_engineconfiguration.objects.all()
    if request.method == "POST":
        engineconfiguration=request.POST.get('txt_EngineConfiguration')
        tbl_engineconfiguration.objects.create(engineconfiguration_value=engineconfiguration)
        return render(request,'Admin/EngineConfiguration.html',{'EngineConfiguration':engineconfdata})
    else:
        return render(request,'Admin/EngineConfiguration.html',{'EngineConfiguration':engineconfdata})
def delEngineConfiguration(request,did):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    tbl_engineconfiguration.objects.get(id=did).delete()
    return redirect('Admin:EngineConfiguration')
def edtEngineConfiguration(request,eid):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    engineconfdata = tbl_engineconfiguration.objects.get(id=eid)
    if request.method == "POST":
        engineconfdata.engineconfiguration_value = request.POST.get('txt_EngineConfiguration')
        engineconfdata.save()
        return redirect('Admin:EngineConfiguration')
    return render(request,'Admin/EngineConfiguration.html',{'EngineConfigurationeditdata':engineconfdata})




def TransmissionType(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    transmissiontypedata=tbl_transmissiontype.objects.all()
    if request.method == "POST":
        transmissiontype=request.POST.get('txt_TransmissionType')
        tbl_transmissiontype.objects.create(transmissiontype_name=transmissiontype)
        return render(request,'Admin/TransmissionType.html',{'TransmissionType':transmissiontypedata})
    else:
        return render(request,'Admin/TransmissionType.html',{'TransmissionType':transmissiontypedata})
def delTransmissionType(request,did):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    tbl_transmissiontype.objects.get(id=did).delete()
    return redirect('Admin:TransmissionType')
def edtTransmissionType(request,eid):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    transmissiontypedata = tbl_transmissiontype.objects.get(id=eid)
    if request.method == "POST":
        transmissiontypedata.transmissiontype_name = request.POST.get('txt_TransmissionType')
        transmissiontypedata.save()
        return redirect('Admin:TransmissionType')
    return render(request,'Admin/TransmissionType.html',{'TransmissionTypeeditdata':transmissiontypedata})



def DriveTrain(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    drivetraindata=tbl_drivetrain.objects.all()
    if request.method == "POST":
        drivetrain=request.POST.get('txt_DriveTrain')
        tbl_drivetrain.objects.create(drivetrain_type=drivetrain)
        return render(request,'Admin/DriveTrain.html',{'DriveTrain':drivetraindata})
    else:
        return render(request,'Admin/DriveTrain.html',{'DriveTrain':drivetraindata})
def delDriveTrain(request,did):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    tbl_drivetrain.objects.get(id=did).delete()
    return redirect('Admin:DriveTrain')
def edtDriveTrain(request,eid):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    drivetraindata = tbl_drivetrain.objects.get(id=eid)
    if request.method == "POST":
        drivetraindata.drivetrain_type = request.POST.get('txt_DriveTrain')
        drivetraindata.save()
        return redirect('Admin:DriveTrain')
    return render(request,'Admin/DriveTrain.html',{'DriveTraineditdata':drivetraindata})



def OwnershipCount(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    ownershipcountdata=tbl_ownershipcount.objects.all()
    if request.method == "POST":
        ownershipcount=request.POST.get('txt_OwnershipCount')
        tbl_ownershipcount.objects.create(OwnershipCount_type=ownershipcount)
        return render(request,'Admin/OwnershipCount.html',{'OwnershipCount':ownershipcountdata})
    else:
        return render(request,'Admin/OwnershipCount.html',{'OwnershipCount':ownershipcountdata})
def delOwnershipCount(request,did):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    tbl_ownershipcount.objects.get(id=did).delete()
    return redirect('Admin:OwnershipCount')
def edtOwnershipCount(request,eid):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    ownershipcountdata = tbl_ownershipcount.objects.get(id=eid)
    if request.method == "POST":
        ownershipcountdata.OwnershipCount_type = request.POST.get('txt_OwnershipCount')
        ownershipcountdata.save()
        return redirect('Admin:OwnershipCount')
    return render(request,'Admin/OwnershipCount.html',{'OwnershipCounteditdata':ownershipcountdata})









def UserList(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    userdata=tbl_user.objects.all()
    return render(request,'Admin/UserList.html',{'userdata':userdata})

def DealerList(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    dealerdata=tbl_dealer.objects.all()
    return render(request,'Admin/DealerList.html',{'dealerdata':dealerdata})
def Acceptdealer(request,aid):
    dealerdata=tbl_dealer.objects.get(id=aid)
    dealerdata.dealer_status=1
    dealerdata.save()
    return render(request,'Admin/DealerList.html',{'msg':"Dealer Accepted"})
def Rejectdealer(request,rid):
    dealerdata=tbl_dealer.objects.get(id=rid)
    dealerdata.dealer_status=2
    dealerdata.save()
    return render(request,'Admin/DealerList.html',{'msg':"Dealer Rejected"})

def ViewComplaint(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    complaintdata=tbl_complaint.objects.filter(complaint_status=0)
    replydata=tbl_complaint.objects.filter(complaint_status=1)
    return render(request,'Admin/ViewComplaint.html',{'complaintdata':complaintdata,'replydata':replydata})

def Reply(request,rid):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    if request.method=="POST":
        reply=tbl_complaint.objects.get(id=rid)
        reply.complaint_reply=request.POST.get('txt_reply')
        reply.complaint_status=1
        reply.save()
        return redirect('Admin:ViewComplaint')
    return render(request,'Admin/Reply.html')

def ViewFeedback(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    feedbackdata=tbl_feedback.objects.all()
    return render(request,'Admin/ViewFeedback.html',{'feedbackdata':feedbackdata})

        

def logout(request):
    del request.session['aid']
    return redirect('Guest:Index')
