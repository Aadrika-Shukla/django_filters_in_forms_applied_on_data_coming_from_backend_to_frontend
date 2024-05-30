from django.shortcuts import render
import datetime

# Create your views here.

# function for testing builtin filters

def builtin_filters(request):
    da=datetime.datetime.now()
    #d={'data':'Hi HoW ARe You','da':da,'c':1}  when c =1 it is showing 1 cat
    d={'data':'Hi HoW ARe You','da':da,'c':2,'m':0}    # now showing 2 cats and 0 mangoes
    d={'data':'Hi HoW ARe You','da':da,'c':0,'m':1,'mco':3,"da":da}     # now showing 2 cats 

    return render(request,'builtin_filters.html',d)
