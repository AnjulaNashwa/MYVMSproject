from django.contrib.auth import logout
from django.shortcuts import render,redirect

from vmsapp.filters import HospitalFilter, VaccineFilter, UserFilter, NurseFilter
from vmsapp.form import nurseform, userform, HospitalForm,VaccineForm,VaccinationcardForm
from vmsapp.models import vaccination,Hospital,Vaccine,Complaint,Bookappointment,Vaccinationcard
from django.contrib import messages



def admin_page(request):
    return render(request,'admintemp/test.html')

def nurse_view(request):
    new = vaccination.objects.filter(is_nurse=True)
    nursefilter=NurseFilter(request.GET,queryset=new)
    new = nursefilter.qs
    context={
        'nurse':new,
        'nursefilter':nursefilter,
    }
    return render(request,'admintemp/nurse_view.html',context)

def nurse_update(request,update):
    updatetable=vaccination.objects.get(id=update)
    updateform=nurseform(instance=updatetable)
    print(updateform)
    if request.method=='POST':
        updateform=nurseform(request.POST,instance=updatetable)
        if updateform.is_valid():
            updateform.save()
            return redirect('View')
    return render(request,'admintemp/nurse_update.html',{'updateform':updateform})


def nurse_delete(request,delete):
    deletetable=vaccination.objects.get(id=delete)
    if request.method == 'POST':
        deletetable.delete()
        return redirect('nurse_view')

def user_view(request):
    new = vaccination.objects.filter(is_user=True)
    userfilter= UserFilter(request.GET,queryset=new)
    new=userfilter.qs
    context = {
        'new':new,
        'userfilter':userfilter
    }
    return render(request,'admintemp/user_view.html',context)

def user_update(request,update):
    updatetable=vaccination.objects.get(id=update)
    updateform=userform(instance=updatetable)
    print(updateform)
    if request.method=='POST':
        updateform=userform(request.POST,instance=updatetable)
        if updateform.is_valid():
            updateform.save()
            return redirect('View')
    return render(request,'admintemp/user_update.html',{'updateform':updateform})


def user_delete(request,delete):
    deletetable=vaccination.objects.get(id=delete)
    if request.method == 'POST':
        deletetable.delete()
        return redirect('user_view')


def hospital(request):
    form = HospitalForm()
    if request.method=='POST':
        form=HospitalForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('hospital_view')
    return render(request,'admintemp/hospital.html',{'form':form})


def hospital_view(request):
    new = Hospital.objects.all()
    hospitalfilter = HospitalFilter(request.GET, queryset=new)
    n = hospitalfilter.qs
    context = {
        'hospital':n,
        'hospitalfilter':hospitalfilter,
    }
    return render(request,'admintemp/hospital_view.html',context)
#
def hospital_update(request,update):
    updatetable=Hospital.objects.get(id=update)
    updateform=HospitalForm(instance=updatetable)
    print(updateform)
    if request.method=='POST':
        updateform=HospitalForm(request.POST,instance=updatetable)
        if updateform.is_valid():
            updateform.save()
            return redirect('View')
    return render(request,'admintemp/hospital_update.html',{'updateform':updateform})
#
def hospital_delete(request,delete):
    deletetable=Hospital.objects.get(id=delete)
    if request.method == 'POST':
        deletetable.delete()
        return redirect('hospital_view')

def vaccine(request):
    form = VaccineForm()
    if request.method=='POST':
        form=VaccineForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('vaccine_view')
    return render(request,'admintemp/vaccine.html',{'form':form})
#
def vaccine_view(request):
    new = Vaccine.objects.all()
    vaccinefilter = VaccineFilter(request.GET,queryset=new)
    new= vaccinefilter.qs
    context = {
        'vaccine':new,
        'vaccinefilter':vaccinefilter,
    }

    return render(request,'admintemp/vaccine_view.html',context)
#
def vaccine_update(request,update):
    updatetable=Vaccine.objects.get(id=update)
    updateform=VaccineForm(instance=updatetable)
    print(updateform)
    if request.method=='POST':
        updateform=VaccineForm(request.POST,instance=updatetable)
        if updateform.is_valid():
            updateform.save()
            return redirect('View')
    return render(request,'admintemp/vaccine_update.html',{'updateform':updateform})
#
#
def vaccine_delete(request,delete):
    deletetable=Vaccine.objects.get(id=delete)
    if request.method == 'POST':
        deletetable.delete()
        return redirect('vaccine_view')





def complaint_viewall(request):
    new = Complaint.objects.all()
    return render(request,'admintemp/complaint_view.html',{'new':new})

def reply_complaints(request, id):
    complaint=Complaint.objects.get(id=id)
    print(complaint)
    if request.method == 'POST':
        r =request.POST.get('reply')
        print(r)
        complaint.reply = r
        complaint.save()

        # message.info(request,'Reply send for complaint')
        return redirect('complaint_viewall')
    return render(request,'admintemp/reply_complaints.html',{'complaint':complaint})

def bookappointmentviewa(request):
    new = Bookappointment.objects.all()
    return render(request,'admintemp/bookappointmentviewa.html',{'new':new})

def approve_appointment(request,id):
    n = Bookappointment.objects.get(id=id)
    n.status = 1
    n.save()
    messages.info(request,'Appointment Confirmed')
    return redirect('bookappointmentviewa')

def reject_appointment(request,id):
    n=Bookappointment.objects.get(id=id)
    n.status=2
    n.save()
    messages.info(request,'Appointment Rejected')
    return redirect('bookappointmentviewa')

def nursebookappointmentview(request):
    new = Bookappointment.objects.filter(status=1).order_by('schedule__date')

    return render(request, 'admintemp/nursebookappointmentview.html', {'new': new})

def vaccinationcard(request,id):
        new = Bookappointment.objects.get(id=id)
        if request.method == 'POST':
            new = VaccinationcardForm(request.POST)
            if new.is_valid():
                new.save()
            return redirect('nursebookappointmentview')
        return render(request, 'admintemp/nursebookappointmentview.html', {'new': new})


def addreportcard(request,id):
    a=Bookappointment.objects.get(id=id)
    print(a)
    a.addreportcard=1
    a.save()
    # messages.info(request,'issued')
    return redirect('nursebookappointmentview')



# def vaccinationcard(request, id):
#     schedule = Bookappointment.objects.get(id=id)
#     appointment =Vaccinationcard.objects.filter()
#     if appointment.exists():
#         messages.info(request, 'you have already requested appointment for this schedule')
#         return redirect('schedule_viewu')
#     else:
#         if request.method == 'POST':
#             obj = Bookappointment()
#             obj.user = data
#             obj.schedule = schedule
#             obj.vaccinename = schedule.vaccinename
#             obj.save()
#             return redirect('schedule_viewu')
#     return render(request,'usertemp/bookappointment.html',{'schedule':schedule})












    # new =Bookappointment.objects.get(id=id)
    # print(new)
    # if request.method == 'POST':
    #     new = VaccinationcardForm(request.POST)
    #     print(new)
    #     if new.is_valid():
    #         new.save()
    #     return redirect('nursebookappointmentview')
    # return render(request,'admintemp/vaccinationcard.html',{'new':new})