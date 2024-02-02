import datetime

from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import vaccination,Hospital,Vaccine,Complaint,Scheduleadd,Bookappointment,Vaccinationcard

class userform(UserCreationForm):
    username=forms.CharField(max_length=250)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=vaccination
        fields=('username','password1','password2','address','childname','childage','gender')

class nurseform(UserCreationForm):
     class Meta:
         model=vaccination
         fields=('username','password1','password2','name','email','address','hospital')

class HospitalForm(forms.ModelForm):
    class Meta:
        model=Hospital
        fields= ('name','place','email','contact')
#
#
#
class VaccineForm(forms.ModelForm):
    class Meta:
        model=Vaccine
        fields=('vaccinename','vaccinetype','description')

# class TimeInput(forms.TimeInput):
#     input_type = 'time'
#
# class DateInput(forms.DateInput):
#     input_type = 'date'
#
# class SheduleaddForm(forms.ModelForm):
#     date=forms.DateField(widget=DateInput)
#     starttime=forms.TimeField(widget=TimeInput, )
#     endtime = forms.TimeField(widget=TimeInput, )
#     class Meta:
#         model=Scheduleadd
#         fields=('hospital','date','vaccinename','starttime','endtime')
#
#     def clean_date(self):
#         cleaned_data = self.cleaned_data
#         date = cleaned_data.get('date')
#         if date and date  != datetime.datetime.date.today():
#             raise forms.ValidationError("Invalid Data")
#         return date

class TimeInput(forms.TimeInput):
    input_type = 'time'

class DateInput(forms.DateInput):
    input_type = 'date'

class SheduleaddForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    starttime = forms.TimeField(widget=TimeInput)
    endtime = forms.TimeField(widget=TimeInput)

    class Meta:
        model = Scheduleadd
        fields = ('hospital', 'date', 'vaccinename', 'starttime', 'endtime')

    def clean_date(self):
        cleaned_data = self.cleaned_data
        date = cleaned_data.get('date')

        if date and date != datetime.date.today():
            raise forms.ValidationError("Invalid Data")

        return date


class ComplaintForm(forms.ModelForm):
    class Meta:
        model=Complaint
        fields=('type','subject','complaints','date')



class VaccinationcardForm(forms.ModelForm):
    class Meta:
        model=Vaccinationcard
        fields=('user','childage','vaccinename','date')