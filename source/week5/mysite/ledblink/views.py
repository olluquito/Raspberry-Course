from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)


def blinker(request):
    if 'on' in request.POST:
        GPIO.output(18,1)
    elif 'off' in request.POST:
        GPIO.output(18,0)
    return render(request,'control_page.html')
