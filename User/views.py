from django.shortcuts import render,redirect
from User.models import*
from Guest.models import*
from Admin.models import*

from decimal import Decimal
from django.http import JsonResponse
import pickle
from datetime import datetime
import pandas as pd

# Create your views here.
def Homepage(request):
    if 'uid' not in request.session:
        return redirect('Guest:login')
    return render(request,'User/Homepage.html')

def ChangePassword(request):
    if 'uid' not in request.session:
        return redirect('Guest:login')
    userpassData=tbl_user.objects.get(id=request.session['uid'])
    if request.method =="POST":
        db_pass=userpassData.user_password
        oldPassword=request.POST.get('txt_CurrentPassword')
        newPassword=request.POST.get('txt_NewPassword')
        confirmpass=request.POST.get('txt_ConfirmPassword')
        if db_pass == oldPassword:
            if newPassword == confirmpass:   
                userpassData.user_password=request.POST.get('txt_NewPassword')
                userpassData.save()
                return redirect('User:UserProfile')
            else:
                return render(request,'User/ChangePassword.html',{'msg':" password  Mismatched"})
        else:
            return render(request,'User/ChangePassword.html',{'msg':"Enter correct password"})
    return render(request,'User/ChangePassword.html')

def UserProfile(request):
    if 'uid' not in request.session:
        return redirect('Guest:login')
    userData=tbl_user.objects.get(id=request.session['uid'])
    return render(request,'User/UserProfile.html',{'userData':userData})

def EditProfile(request):
    if 'uid' not in request.session:
        return redirect('Guest:login')
    UserpData=tbl_user.objects.get(id=request.session['uid'])
    if request.method =="POST":
        UserpData.user_name=request.POST.get('txt_name')
        UserpData.user_contact=request.POST.get('txt_contact')
        UserpData.user_address=request.POST.get('txt_address')
        UserpData.save()
        return redirect('User:UserProfile')
    return render(request,'User/EditProfile.html',{'UserpData':UserpData})

def Complaint(request):
    if 'uid' not in request.session:
        return redirect('Guest:login')
    complaintdata=tbl_complaint.objects.filter(user_id=request.session['uid'])
    if request.method=="POST":
        title=request.POST.get("txt_title")
        content=request.POST.get("txt_Content")
        user=tbl_user.objects.get(id=request.session['uid'])
        tbl_complaint.objects.create(complaint_title=title,complaint_content=content,user_id=user)
        return render(request,'User/Complaint.html',{'complaintdata':complaintdata})
    else:
        return render(request,'User/Complaint.html',{'complaintdata':complaintdata})
    
def Message(request,vid):
    if 'uid' not in request.session:
        return redirect('Guest:login')
    message=tbl_message.objects.filter(vehicle_id=vid,user_id=request.session['uid'])
    if request.method=="POST":
        title=request.POST.get("txt_title")
        content=request.POST.get("txt_Content")
        user=tbl_user.objects.get(id=request.session['uid'])
        vehicle=tbl_vehicle.objects.get(id=vid)
        tbl_message.objects.create(message_title=title,message_content=content,user_id=user,vehicle_id=vehicle)
        return render(request,'User/Message.html',{'message':message})
    else:
        return render(request,'User/message.html',{'message':message})
    
def ViewVehicle(request):
    if 'uid' not in request.session:
        return redirect('Guest:login')
    companydata=tbl_company.objects.all()

    vehicledata=tbl_vehicle.objects.all()
    return render(request,'User/ViewVehicle.html',{'vehicledata':vehicledata,'companydata':companydata})

def ViewVehicledetails(request,vid):
    if 'uid' not in request.session:
        return redirect('Guest:login')
    vehicledata=tbl_vehicle.objects.get(id=vid)
    return render(request,'User/ViewVehicledetails.html',{'vehicledetdata':vehicledata})
def Booking(request, vid):
    vehicleid = tbl_vehicle.objects.get(id=vid)
    userid = tbl_user.objects.get(id=request.session['uid']) 
    booking_amount = vehicleid.vehicle_price * Decimal('0.10')
    if request.method == "POST":
        tbl_booking.objects.create(vehicle_id=vehicleid,user_id=userid,booking_amount=booking_amount)

        return render(request, 'User/BookingConfirmation.html',{'vehicleid':vehicleid,'msg':"Vehicle Booked"})


    return render(request, 'User/BookingConfirmation.html',{'vehicleid':vehicleid})

    

def MyBooking(request):
    if 'uid' not in request.session:
        return redirect('Guest:login')
    bookdata=tbl_booking.objects.filter(user_id=request.session['uid'])
    return render(request,'User/MyBooking.html',{'bookdata':bookdata})

def DealerDetails(request,did):
    if 'uid' not in request.session:
        return redirect('Guest:login')
    dealerData=tbl_dealer.objects.get(id=did)
    return render(request,'User/DealerDetails.html',{'dealerData':dealerData})


def Feedback(request):
    if 'uid' not in request.session:
        return redirect('Guest:login')
    feedbackdata=tbl_feedback.objects.filter(user_id=request.session['uid'])
    if request.method=="POST":
        content=request.POST.get("txt_Content")
        user=tbl_user.objects.get(id=request.session['uid'])
        tbl_feedback.objects.create(feedback_content=content,user_id=user)
        return render(request,'User/Feedback.html',{'feedbackdata':feedbackdata})
    else:
        return render(request,'User/Feedback.html',{'feedbackdata':feedbackdata})   
def delFeedback(request,did):
    if 'uid' not in request.session:
        return redirect('Guest:login')
    tbl_feedback.objects.get(id=did).delete()
    return redirect('User:Feedback')


def ajaxmodel(request):
    model = tbl_model.objects.filter(company=request.GET.get('did'))
    return render(request, "User/AjaxModel.html",{'model':model})

def ajaxvech(request):
    vehicledata = tbl_vehicle.objects.filter(vehicle_model_name=request.GET.get('mid'))
    return render(request, "User/AjaxVehicle.html",{'vehicledata':vehicledata})


def payment(request,vid):
    amount=tbl_booking.objects.get(id=vid)
    counts = tbl_booking.objects.filter(id=vid,user_id=request.session["uid"],booking_status=3).count()
    print(counts)
    if counts > 0:
        return render(request,"User/Payment.html",{"msg":"Payment Already Done.."})
    else:
        if request.method == "POST":
            amount.booking_status=3
            amount.save()
            return redirect("User:loader")
        else:
            return render(request,"User/Payment.html",{'amount':amount})

def loader(request):
    return render(request,"User/Loader.html")

def paymentsuc(request):
    return render(request,"User/Paymentsuc.html")



def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(vehicle=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(vehicle=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(user=tbl_user.objects.get(id=request.session['uid']),user_review=user_review,rating_data=rating_data,vehicle=tbl_vehicle.objects.get(id=pid))
    stardata=tbl_rating.objects.filter(vehicle=pid).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(vehicle=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(vehicle=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)

def logout(request):
    del request.session['uid']
    return redirect('Guest:Index')

def ViewGallery(request,gid):
    gallery=tbl_gallery.objects.filter(vehicle=gid)
    return render(request,"User/ViewGallery.html",{'gallery':gallery})



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

    return render(request,"User/PricePrediction.html",{"price":price,'companydata':companydata,'Modelyear':modelyeardata})