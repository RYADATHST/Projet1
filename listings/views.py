from django.shortcuts import render
from django.http import HttpResponse
from listings.forms import ContactUsForm
from listings.models import Domaine
import requests
import whois

def ldmapi(request):
    form = ContactUsForm()
    if request.method =='POST':
        domain_name = request.POST.get("nom")
        domain_name_str= str(domain_name)
        domain_info = whois.whois(domain_name_str)
        return render(request, 'listings/whois.html',{'form': form,'domain_info': domain_info})
    return render(request, 'listings/base.html',{'form': form})
    


# Create your views here.
