import django_filters
from django import forms
from django_filters import CharFilter
from vmsapp.models import Hospital, Vaccine, vaccination, Complaint,Scheduleadd


class HospitalFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name',label="",lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder':'Search Name','class':'form-control'}))

    class Meta:
        model = Hospital
        fields = ('name',)

class VaccineFilter(django_filters.FilterSet):
    name = CharFilter(field_name='vaccinename',label="",lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder':'Search Name','class':'form-control'}))

    class Meta:
        model = Vaccine
        fields = ('name',)

class UserFilter(django_filters.FilterSet):
    name=CharFilter(field_name='username',label="",lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))

    class Meta:
        model = vaccination
        fields=('name',)


class NurseFilter(django_filters.FilterSet):
    name=CharFilter(field_name='name',label="",lookup_expr='icontains',widget=forms.TextInput(attrs={
    'placeholder': 'Search Name', 'class': 'form-control'}))

    class Meta:
        model = vaccination
        fields=('name',)

#nurseview#
class VaccineFilter(django_filters.FilterSet):
    name = CharFilter(field_name='vaccinename', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))

    class Meta:
        model = Vaccine
        fields = ('name',)

# class UserFilter(django_filters.FilterSet):
#     name=CharFilter(field_name='name',label="",lookup_expr='icontains',widget=forms.TextInput(attrs={
#         'placeholder': 'Search Name', 'class': 'form-control'}))
#
#     class Meta:
#         model = vaccination
#         fields=('name',)

class HospitalFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name',label="",lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder':'Search Name','class':'form-control'}))

    class Meta:
        model = Hospital
        fields = ('name',)

class ComplaintFilter(django_filters.FilterSet):
    name = CharFilter(field_name='date',label="",lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder':'Search Name','class':'form-control'}))

    class Meta:
        model = Complaint
        fields = ('name',)


class ScheduleFilter(django_filters.FilterSet):
    name = CharFilter(field_name='date',label="",lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder':'Search Name','class':'form-control'}))

    class Meta:
        model = Scheduleadd
        fields = ('name',)

class ComplaintsFilter(django_filters.FilterSet):
    name = CharFilter(field_name='date',label="",lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder':'Search Name','class':'form-control'}))

    class Meta:
        model = Complaint
        fields = ('name',)
