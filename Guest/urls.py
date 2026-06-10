from django.urls import path
from Guest import views
app_name = "Guest"
urlpatterns = [

    
    path("Login/",views.Login,name="login"),

    path("NewUser/",views.NewUser,name="NewUser"),

    path("NewDealer/",views.NewDealer,name="NewDealer"),
    path("ajaxplace/",views.ajaxplace,name="ajaxplace"),
    path("Index/",views.Index,name="Index"),
    path('PricePrediction/',views.predict_car_price,name="PricePrediction"),
    path('Signup/',views.Signup,name="Signup"),


]