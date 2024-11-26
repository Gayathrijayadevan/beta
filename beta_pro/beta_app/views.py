from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(req):
    data=Course.objects.all()[:3]
    return render(req,'index.html',{'cours':data})
   
def contact(req):
    return render(req,'contact.html')

def about(req):
    return render(req,'about.html')

def courses_dtl(req,c_id):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        message=req.POST['message']
        subject=req.POST['subject']
        phone=req.POST['phone']
        data=Contact.objects.create(name=name,email=email,message=message,subject=subject,Phone=phone)
        data.save()
        return redirect(index)
    
    data=Course.objects.get(pk=c_id)
    return render (req,'cors_dtl.html',{'courses':data})

def contact(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        message=req.POST['message']
        subject=req.POST['subject']
        phone=req.POST['phone']
        data=Contact.objects.create(name=name,email=email,message=message,subject=subject,Phone=phone)
        data.save()
        return redirect(contact)
    else:
        return render (req,'contact.html')
    
def view_course(req,):
    data=Course.objects.all()
    return render(req,'view_course.html',{'v_courses':data})


