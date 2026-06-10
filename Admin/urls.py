from django.urls import path
from Admin import views
app_name='Admin'
urlpatterns = [


    path("District/",views.District,name="District"),
    path("AdminRegistration/",views.AdminRegistration,name="AdminRegistration"),
    path("Place/",views.Place,name="Place"),
    path("Homepage/",views.Homepage,name="Homepage"),
    path("ChangePassword/",views.ChangePassword,name="ChangePassword"),
    path("Company/",views.Company,name="Company"),
    path("ModelName/",views.ModelName,name="ModelName"),
    path("ModelYear/",views.ModelYear,name="ModelYear"),
    path("BodyType/",views.BodyType,name="BodyType"),
    path("SeatingCapacity/",views.SeatingCapacity,name="SeatingCapacity"),
    path("DoorCount/",views.DoorCount,name="DoorCount"),
    path("FuelType/",views.FuelType,name="FuelType"),
    path("EngineConfiguration/",views.EngineConfiguration,name="EngineConfiguration"),
    path("TransmissionType/",views.TransmissionType,name="TransmissionType"),
    path("DriveTrain/",views.DriveTrain,name="DriveTrain"),
    path("OwnershipCount/",views.OwnershipCount,name="OwnershipCount"),
    path("UserList/",views.UserList,name="UserList"),
    path("DealerList/",views.DealerList,name="DealerList"),
    path("ViewComplaint/",views.ViewComplaint,name="ViewComplaint"),
    path("ViewFeedback/",views.ViewFeedback,name="ViewFeedback"),


    path("delDistrict/<int:did>",views.delDistrict,name="delDistrict"),
    path("delAdminRegistration/<int:did>",views.delAdminRegistration,name="delAdminRegistration"),
    path("delPlace/<int:did>",views.delPlace,name="delPlace"),
    path("delDoorcount/<int:did>",views.delDoorcount,name="delDoorcount"),
    path("delCompany/<int:did>",views.delCompany,name="delCompany"),
    path("delModelName/<int:did>",views.delModelName,name="delModelName"),
    path("delModelYear/<int:did>",views.delModelYear,name="delModelYear"),
    path("delBodyType/<int:did>",views.delBodyType,name="delBodyType"),
    path("delSeatingCapacity/<int:did>",views.delSeatingCapacity,name="delSeatingCapacity"),
    path("delFuelType/<int:did>",views.delFuelType,name="delFuelType"),
    path("delEngineConfiguration/<int:did>",views.delEngineConfiguration,name="delEngineConfiguration"),
    path("delTransmissionType/<int:did>",views.delTransmissionType,name="delTransmissionType"),
    path("delDriveTrain/<int:did>",views.delDriveTrain,name="delDriveTrain"),
    path("delOwnershipCount/<int:did>",views.delOwnershipCount,name="delOwnershipCount"),
    
    path("edtDistrict/<int:eid>",views.edtDistrict,name="edtDistrict"),
    path("edtAdminRegistration/<int:eid>",views.edtAdminRegistration,name="edtAdminRegistration"),
    path("edtPlace/<int:eid>",views.edtPlace,name="edtPlace"),
    path("edtCompany/<int:eid>",views.edtCompany,name="edtCompany"),
    path("edtModelName/<int:eid>",views.edtModelName,name="edtModelName"),
    path("edtModelYear/<int:eid>",views.edtModelYear,name="edtModelYear"),
    path("edtBodyType/<int:eid>",views.edtBodyType,name="edtBodyType"),
    path("edtSeatingCapacity/<int:eid>",views.edtSeatingCapacity,name="edtSeatingCapacity"),
    path("edtDoorcount/<int:eid>",views.edtDoorcount,name="edtDoorcount"),
    path("edtFuelType/<int:eid>",views.edtFuelType,name="edtFuelType"),
    path("edtEngineConfiguration/<int:eid>",views.edtEngineConfiguration,name="edtEngineConfiguration"),
    path("edtTransmissionType/<int:eid>",views.edtTransmissionType,name="edtTransmissionType"),
    path("edtDriveTrain/<int:eid>",views.edtDriveTrain,name="edtDriveTrain"),
    path("edtOwnershipCount/<int:eid>",views.edtOwnershipCount,name="edtOwnershipCount"),
    path("Reply/<int:rid>",views.Reply,name="Reply"),
    
    path("Acceptdealer/<int:aid>",views.Acceptdealer,name="Acceptdealer"),
    path("Rejectdealer/<int:rid>",views.Rejectdealer,name="Rejectdealer"),
    path("logout/",views.logout,name="logout"),
  


    



]