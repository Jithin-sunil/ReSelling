from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from decimal import Decimal
from django.http import JsonResponse
import pickle
from datetime import datetime
import pandas as pd

# Create your views here.


def Login(request):
    if request.method == "POST":
        email = request.POST.get('txt_email')
        password = request.POST.get('txt_password')

        admincount = tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        dealercount = tbl_dealer.objects.filter(dealer_email=email,dealer_password=password).count()
        usercount = tbl_user.objects.filter(user_email=email,user_password=password).count()

        if admincount > 0:
            admin = tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid'] = admin.id
            return redirect('Admin:Homepage')
        elif dealercount > 0:
            dealer =tbl_dealer.objects.get(dealer_email=email,dealer_password=password)
            if dealer.dealer_status==1:
                request.session['dlrid'] = dealer.id
                return redirect('Dealer:Homepage')
            elif dealer.dealer_status==2:
                return render(request,'Guest/Login.html',{"msg":"Dealer Rejected"})
            elif dealer.dealer_status==0 :
                return render(request,'Guest/Login.html',{"msg":"Authentication Pending"})
            else:
                return render(request,'Guest/Login.html',{"msg":"Invalid Login"})

        elif usercount > 0:
            user =tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid'] = user.id
            return redirect('User:Homepage')
        else:
            return render(request,'Guest/Login.html',{"msg":"Invalid Login"})
    return render(request,'Guest/Login.html')

def NewUser(request):
    districtdata = tbl_district.objects.all()
    if request.method=='POST':
        name=request.POST.get('txt_name')
        contact= request.POST.get('txt_contact')
        email =request.POST.get('txt_email')
        password=request.POST.get('txt_password')
        confirmpassword=request.POST.get('txt_confirmpassword')
        address=request.POST.get('txt_Address')
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        place=tbl_place.objects.get(id=request.POST.get('sel_place'))
        photo=request.FILES.get('img_photo')
        proof=request.FILES.get('img_proof')
        if password == confirmpassword:
            userData=tbl_user.objects.filter(user_email=email).count()
            if userData > 0:
                return render(request,'Guest/NewUser.html',{'msg':"User Already Registered"})
            else:
                tbl_user.objects.create(user_name=name,user_contact=contact,user_email=email,user_password=password,user_address=address,user_place=place,user_photo=photo,user_proof=proof)
                return render(request,'Guest/NewUser.html',{'msg':"Registration Completed"})
        else:
            return render(request,'Guest/NewUser.html',{'msg':"Enter correct password"})
    else:
        return render(request,'Guest/NewUser.html',{'Districtdata':districtdata})

def NewDealer(request):
    districtdata = tbl_district.objects.all()
    if request.method=='POST':
        name=request.POST.get('txt_name')
        contact= request.POST.get('txt_contact')
        email =request.POST.get('txt_email')
        password=request.POST.get('txt_password')
        confirmpassword=request.POST.get('txt_ConfirmPassword')
        address=request.POST.get('txt_Address')
        place=tbl_place.objects.get(id=request.POST.get('sel_place'))
        LicenseNumber=request.POST.get('txt_LicenseNumber')
        EstablishDate=request.POST.get('txt_EstablishDate')
        OwnerName=request.POST.get('txt_OwnerName')
        OwnerContactNumber=request.POST.get('txt_OwnerContactNumber')
        OwnerAadharnumber=request.POST.get('txt_OwnerAadharnumber')
        LicenseProof=request.FILES.get('img_LicenseProof')
        OwnerProof=request.FILES.get('img_OwnerProof')
        OwnerPhoto=request.FILES.get('img_OwnerPhoto')
        Logo=request.FILES.get('img_Logo')
        if password == confirmpassword:
            dealerData=tbl_dealer.objects.filter(dealer_email=email).count()
            if dealerData>0:
                    return render(request,'Guest/NewDealer.html',{'msg':"Dealer Already Registered"})
            else:
                tbl_dealer.objects.create(dealer_name=name,dealer_contact=contact,dealer_email=email,dealer_password=password,dealer_address=address,dealer_place=place,license_no=LicenseNumber,establish_date=EstablishDate,owner_name=OwnerName,owner_contact=OwnerContactNumber,owner_aadhar_no=OwnerAadharnumber,owner_photo=OwnerPhoto,owner_proof=OwnerProof,license_proof=LicenseProof,dealer_logo=Logo)
                return render(request,'Guest/NewDealer.html',{'msg':"Registration Completed"})
        else:
            return render(request,'Guest/NewDealer.html',{'msg':"Enter correct password"})
    else:
        return render(request,'Guest/NewDealer.html',{'District':districtdata})
    
    
def ajaxplace(request):
    place = tbl_place.objects.filter(district_name=request.GET.get('did'))
    return render(request, "Guest/Ajaxplace.html",{'place':place})

def Index(request):
    return render(render,"Guest/Index.html")

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

    return render(request,"Guest/PricePrediction.html",{"price":price,'companydata':companydata,'Modelyear':modelyeardata})


def Signup(request):
    return render(render,"Guest/Signup.html")    