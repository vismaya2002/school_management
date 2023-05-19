from django.urls import path
from .views import details,create,update,deletedata,getdata,total

urlpatterns = [
    path('api/student/<int:pk>',details),
    path('api/student/create/',create),
    path('api/student/update/<int:pk>',update),
    path('api/student/delete/<int:pk>',deletedata),
    path('api/student/displayall/',getdata),
    path('api/student/total/',total)

]