from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import StudentDetails
from .serializers import StudentDetailserializer
from django.http import JsonResponse
# Create your views here.

@api_view(['POST'])
def create(request):
    serializer = StudentDetailserializer(data=request.data)
    if serializer.is_valid():
        serializer.save() 
        return Response(status= status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def details(request,pk):
    try:
        id = StudentDetails.objects.get(student_id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    srid = StudentDetailserializer(id)
    return Response(srid.data,status=status.HTTP_200_OK)

@api_view(['PUT'])
def update(request,pk):
    try:
        serializer = StudentDetails.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    srupdate = StudentDetailserializer(serializer,data=request.data)
    if srupdate.is_valid():
        srupdate.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deletedata(request,pk):
    try:
        data = StudentDetails.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data.delete()
    return Response(status=status.HTTP_200_OK)
   
@api_view(['GET'])
def getdata(request):
    try:
        dataz = StudentDetails.objects.all()
    except StudentDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    srdata = StudentDetailserializer(dataz,many=True)
    return Response(srdata.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def total(request):
    try:
        datas = StudentDetails.objects.all()
        context = {
            'total_students' : len(datas)
        }
        return JsonResponse(context)
    except StudentDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

