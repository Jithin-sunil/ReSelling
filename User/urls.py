from django.urls import path
from User import views
app_name='User'
urlpatterns = [


path("Homepage/",views.Homepage,name="Homepage"),   
path("ChangePassword/",views.ChangePassword,name="ChangePassword"),
path("UserProfile/",views.UserProfile,name="UserProfile"),
path("EditProfile/",views.EditProfile,name="EditProfile"),
path("Complaint/",views.Complaint,name="Complaint"),
path("ViewVehicle/",views.ViewVehicle,name="ViewVehicle"),
path("ViewVehicledetails/<int:vid>",views.ViewVehicledetails,name="ViewVehicledetails"),
path("BookingConfirmation/<int:vid>",views.Booking,name="BookingConfirmation"),
path("MyBooking/",views.MyBooking,name="MyBooking"),
path('DealerDetails/<int:did>',views.DealerDetails,name="DealerDetails"),  
path('rating/<int:mid>',views.rating,name="rating"),  
path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
path('starrating/',views.starrating,name="starrating"),
path('Feedback/',views.Feedback,name="Feedback"),
path('delFeedback/<int:did>',views.delFeedback,name="delFeedback"),  
path("ajaxmodel/",views.ajaxmodel,name="ajaxmodel"),
path("ajaxvech/",views.ajaxvech,name="ajaxvech"),

 path("payment/<int:vid>",views.payment,name="payment"),
    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'),

path("logout/",views.logout,name="logout"),
path('ViewGallery/<int:gid>',views.ViewGallery,name="ViewGallery"),  
path('Message/<int:vid>',views.Message,name="Message"), 
path('PricePrediction/',views.predict_car_price,name="PricePrediction"),





]