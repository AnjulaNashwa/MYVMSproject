from django.shortcuts import render, redirect

from vmsapp.filters import VaccineFilter, UserFilter, HospitalFilter, ComplaintFilter, ScheduleFilter, ComplaintsFilter
from vmsapp.models import Vaccine, vaccination, Hospital, Complaint, Scheduleadd, Bookappointment

from vmsapp.form import ComplaintForm, SheduleaddForm
from django.contrib import messages
from django.http import Http404


def vaccine_viewn(request):
    new = Vaccine.objects.all()
    vaccinefilter = VaccineFilter(request.GET, queryset=new)
    new = vaccinefilter.qs
    context = {
        'vaccine': new,
        'vaccinefilter': vaccinefilter
    }
    return render(request, 'nursetemp/vaccine_viewn.html', context)


def user_viewn(request):
    new = vaccination.objects.filter(is_user=True)
    userfilter = UserFilter(request.GET, queryset=new)
    new = userfilter.qs
    context = {
        'user': new,
        'userfilter': userfilter
    }
    return render(request, 'nursetemp/user_viewn.html', context)


def hospital_viewn(request):
    new = Hospital.objects.all()
    hospitalfilter = HospitalFilter(request.GET, queryset=new)
    new = hospitalfilter.qs
    context = {
        'hospital': new,
        'hospitalfilter': hospitalfilter
    }
    return render(request, 'nursetemp/hospital_viewn.html', context)


def complaintregister(request):
    form = ComplaintForm()
    var = request.user
    print(var)
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = var
            obj.save()
            return redirect('complaintregister')
    return render(request, 'nursetemp/complaintregister.html', {'form': form})







def complaint_viewn(request):
    n = Complaint.objects.filter(type=request.user)
    complaintsfilter = ComplaintsFilter(request.GET, queryset=n)
    n = complaintsfilter.qs
    context = {
        'complaints': n,
        'complaintsfilter': complaintsfilter
    }
    return render(request, 'nursetemp/complaint_viewn.html', context)

def scheduleadd(request):
    form = SheduleaddForm()
    if request.method == 'POST':
        form = SheduleaddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_viewn')
    return render(request, 'nursetemp/scheduleadd.html', {'form': form})


def scheduleadd_update(request, update):
    updatetable = Scheduleadd.objects.get(id=update)
    updateform = SheduleaddForm(instance=updatetable)
    print(updateform)
    if request.method == 'POST':
        updateform = SheduleaddForm(request.POST, instance=updatetable)
        if updateform.is_valid():
            updateform.save()
            return redirect('schedule_viewn')
    return render(request, 'nursetemp/scheduleadd_update.html', {'updateform': updateform})


def scheduleadd_delete(request, delete):
    deletetable = Scheduleadd.objects.get(id=delete)
    if request.method == 'POST':
        deletetable.delete()
        return redirect('scheduleadd_viewn')


def schedule_viewn(request):
    new = Scheduleadd.objects.all()
    schedulefilter = ScheduleFilter(request.GET, queryset=new)
    new = schedulefilter.qs
    context = {
        'new': new,
        'schedulefilter': schedulefilter
    }
    return render(request, 'nursetemp/schedule_viewn.html',context)


def bookappointmentstatusviewn(request):
    new = Bookappointment.objects.filter(status=1)
    return render(request, 'nursetemp/bookappointmentstatusviewn.html', {'new': new})


from django.http import Http404


def markvaccinated(request, id):
    appointment = Bookappointment.objects.get(id=id)
    appointment.vaccinated = True
    appointment.save()
    messages.info(request, 'Vaccinated')
    return redirect('bookappointmentstatusviewn')
