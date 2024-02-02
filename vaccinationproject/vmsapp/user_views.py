from django.contrib import messages
from django.shortcuts import render,redirect

from vmsapp.filters import ScheduleFilter, ComplaintFilter
from vmsapp.models import Complaint,Scheduleadd,Bookappointment,vaccination
from vmsapp.form import ComplaintForm, userform


def complaint_registeru(request):
    form = ComplaintForm()
    if request.method=='POST':
        form=ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('complaint_registeru')
    return render(request,'usertemp/complaint_registeru.html',{'form':form})

def complaint_viewu(request):
    u = Complaint.objects.filter(type =request.user)
    complaintfilter = ComplaintFilter(request.GET, queryset=u)
    u = complaintfilter.qs
    context = {
        'complaints': u,
        'complaintfilter': complaintfilter
    }
    return render(request,'usertemp/complaint_viewu.html',context)

def schedule_viewu(request):
    new = Scheduleadd.objects.all()
    schedulefilter = ScheduleFilter(request.GET, queryset=new)
    new = schedulefilter.qs
    context = {
        'new': new,
        'schedulefilter': schedulefilter
    }
    return render(request,'usertemp/schedule_viewu.html',context)

def bookappointment(request, id):
    schedule = Scheduleadd.objects.get(id=id)
    data = request.user
    appointment =Bookappointment.objects.filter(user_id=data,schedule=schedule)
    if appointment.exists():
        messages.info(request, 'you have already requested appointment for this schedule')
        return redirect('schedule_viewu')
    else:
        if request.method == 'POST':
            obj = Bookappointment()
            obj.user = data
            obj.schedule = schedule
            obj.vaccinename = schedule.vaccinename
            obj.save()
            return redirect('schedule_viewu')
    return render(request,'usertemp/bookappointment.html',{'schedule':schedule})

def bookappointmentstatusviewu(request):
    u=request.user
    new = Bookappointment.objects.filter(user=u)
    return render(request,'usertemp/bookappointmentstatusviewu.html',{'new':new})

def profile(request):
    new = vaccination.objects.filter(username=request.user).first()
    return render(request,'usertemp/profile.html',{'new':new})

def profileupdate(request,update):
    updatetable=vaccination.objects.get(id=update)
    updateform=userform(instance=updatetable)
    print(updateform)
    if request.method=='POST':
        updateform=userform(request.POST,instance=updatetable)
        if updateform.is_valid():
            updateform.save()
            return redirect('profile')
    return render(request,'usertemp/profileupdate.html',{'updateform':updateform})
#
#




