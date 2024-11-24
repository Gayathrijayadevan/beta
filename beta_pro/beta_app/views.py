from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'index.html')
    
def contact(req):
    return render(req,'contact.html')

def about(req):
    return render(req,'about.html')

def cour_dtl(req):
    return render(req,'cors_dtl.html')

