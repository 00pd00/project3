from django.shortcuts import render
from django.shortcuts import render , HttpResponseRedirect , redirect ,HttpResponse
from .models import appt
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import apptSerializer



class apptViewSet(viewsets.ModelViewSet):
    queryset = appt.objects.all()
    serializer_class = apptSerializer

def index(request):
    if request.method=='POST':
        date=request.POST['date']
        time=request.POST['time']
        var=appt(date=date,time=time)
        var.save()
        return HttpResponse('Appointment booked')


    return render(request,'book.html')

