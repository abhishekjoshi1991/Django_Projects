from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import addstud
from .models import addstudent
from django.contrib import messages
# Create your views here.

# below func will add items and show items
def add_show(request):
    if request.method =="POST":
        form = addstud(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']
            modobject = addstudent(name=nm,email=em,password=pw)
            modobject.save()
            form = addstud() #to empty the form after adding the entry
            messages.success(request, 'Student Added Successfully.')
    else:
        form = addstud()
    stud = addstudent.objects.all()
    return render(request,'addandshow.html',{'form':form,'stud':stud,'add':'ADD','message':'added'})


#this will update/edit entries from DB
def update_data(request,id):
    if request.method=="POST":
        getdata = addstudent.objects.get(pk=id) #get data for specific id and then pass it as instance below
        form = addstud(request.POST, instance=getdata)
        if form.is_valid():
            form.save()
            form = addstud()
            stud = addstudent.objects.all()
            messages.success(request, 'Record Updated successfully.')
            return redirect('/')
    else: #if method is GET then
        getdata = addstudent.objects.get(pk=id)
        form = addstud(instance=getdata) #display form with instance data
    stud = addstudent.objects.all()
    return render(request,'addandshow.html',{'form':form,'stud':stud,'add':'UPDATE','message':'updated'})


#this function will delete entries
def delete_data(request,id):
    studobj = addstudent.objects.get(pk=id) #pk- priary key
    studobj.delete()
    return HttpResponseRedirect('/') #redirect to home page i.e /crud


