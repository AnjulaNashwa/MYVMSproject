from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import vaccination


from vmsapp.form import userform,nurseform

# Create your views here.
# def index(request):
#     return HttpResponse("WELLCOME")

def index(request):
    return render(request,'index.html')


def login_view(request):
    if request.method=='POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user1 = authenticate(request,username=username,password=password)
        if user1 is not None:
            login(request, user1)
            print("hello")
            if user1.is_staff:
                return redirect('adminpage')
            elif user1.is_user:
                return redirect('userpage')
            elif user1.is_nurse:
                return redirect('nursepage')
        else:
            messages.error(request,'INVALID ERROR')
    return render(request,'login.html')

def userpage(request):
    return render(request,'usertemp/base.html')



def user_reg(request):
    form=userform()
    if request.method=='POST':
        form=userform(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_user=True
            user.save()
            return redirect('index')
    return render(request,'user_reg.html',{'form':form})


def nurse_reg(request):
    form = nurseform()
    if request.method == 'POST':
        form = nurseform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_nurse = True
            user.save()
            return redirect('index')
    return render(request, 'nurse_reg.html', {'form':form})



def adminpage(request):
    return render(request,'admintemp/test.html')
def nursepage(request):
    return render(request,'nursetemp/base.html')

def nurse_update(request,update):
    updatetable=vaccination.objects.get(id=update)
    updateform=nurseform(instance=updatetable)
    print(updateform)
    if request.method=='POST':
        updateform=nurseform(request.POST,instance=updatetable)
        if updateform.is_valid():
            updateform.save()
            return redirect('View')
    return render(request,'nurse_update.html',{'updateform':updateform})

# def nurse_view(request):
#     new = vaccination.objects.all()
#     print(new)
#     return render(request,'nurse_view.html',{'new':new})


def logout_view(request):
    logout(request)
    return redirect('index.html')

def delete(request,delete):
    deletetable=vaccination.objects.get(id=delete)
    deletetable.delete()
    return redirect('View')