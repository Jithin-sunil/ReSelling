from django.urls import path
from Dealer import views
app_name="Dealer"
urlpatterns = [


    path("Homepage/",views.Homepage,name="Homepage"),
    path("VehicleRegistration/",views.VehicleRegistration,name="VehicleRegistration"),
    path("ChangePassword/",views.ChangePassword,name="ChangePassword"),
    path("DealerProfile/",views.DealerProfile,name="DealerProfile"),
    path("EditProfile/",views.EditProfile,name="EditProfile"),
    path("MyVehicles/",views.MyVehicles,name="MyVehicles"),
    path("delMyVehicles/<int:did>",views.delMyVehicles,name="delMyVehicles"),
    path("AddGallery/<int:vid>",views.AddGallery,name="AddGallery"),
    path("delAddGallery/<int:did>",views.delAddGallery,name="delAddGallery"),
    path("ViewBooking/",views.ViewBooking,name="ViewBooking"),
    path("UserDetails/<int:uid>",views.UserDetails,name="UserDetails"),
    path("ajaxmodel/",views.ajaxmodel,name="ajaxmodel"),
    path("acptViewBooking/<int:aid>",views.acptViewBooking,name="acptViewBooking"),
    path("rejctViewBooking/<int:rid>",views.rejctViewBooking,name="rejctViewBooking"),
    path("logout/",views.logout,name="logout"),
    path("ViewMessages/",views.ViewMessages,name="ViewMessages"),
    path("Reply/<int:rid>",views.Reply,name="Reply"),
    path('PricePrediction/',views.predict_car_price,name="PricePrediction"),
]