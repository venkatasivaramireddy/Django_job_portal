from urllib import request
from django.contrib import messages
from django.contrib.messages.storage import session
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from django.views.generic import CreateView, FormView, UpdateView
from app.models import StudentModel,JobDetails
from app.form import StudentForm,JobDetailsForm

def loginPage(request):
    try:
        value=request.session["email"]
    except KeyError:
        student = StudentForm()
        return render(request, "reg.html", {"form": student})
    else:
        return homepage(request)


def homepage(request):
    try:
        value = request.session["email"]
    except KeyError:
        messages.success(request, "Please login")
        return redirect("main")
    else:
        return render(request,"welcome.html",{"email":value})

def savedetails(request):
    try:
        n=request.POST["name"]
        e=request.POST["email"]
        p=request.POST["password"]
        i=request.FILES["photo"]
        StudentModel(name=n,email=e,password=p,photo=i).save()
        messages.success(request,"registered Successfully, Please Login To access Dashboard")
        return redirect("main")
    except:
        messages.success(request, "Email Already Exstised Please login")
        return redirect("main")

def verityuser(request):
    e = request.POST["email"]
    p = request.POST["password"]
    try:
        res=StudentModel.objects.get(email=e,password=p)
    except StudentModel.DoesNotExist:
        messages.success(request, "Details Not Match Please register")
        return redirect("main")
    else:
        request.session["email"] = e
        return redirect("welcome")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def postjob(request):
    try:
        value = request.session["email"]
    except KeyError:
        messages.success(request, "Please login")
        return redirect("main")
    else:
        details = JobDetailsForm()
        return render(request, "postjob.html", {"jobform": details})

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def savejob(request):
    t = request.POST["title"]
    d = request.POST["description"]
    i = request.FILES["image"]
    JobDetails(title=t,description=d,image=i).save()
    messages.success(request,"Job Posted Successfuly")
    return redirect("viewjobs")

from django.core.paginator import Paginator
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewjobs(request):
    try:
        value = request.session["email"]
    except KeyError:
        messages.success(request, "Please login")
        return redirect("main")
    else:
        pno = request.GET.get("page_no")
        list = JobDetails.objects.all()
        p = Paginator(list, 3)
        if pno:
            pge = p.page(pno)
        else:
            pge = p.page(1)
        return render(request, "viewjob.html", {"page": pge})

def profile(request):
    try:
        value = request.session["email"]
    except KeyError:
        messages.success(request, "Please login")
        return redirect("main")
    else:
        value = StudentModel.objects.get(email=value)
        return render(request,"profile.html",{"profile":value})


def offcampusdrive(request):
    try:
        value = request.session["email"]
    except KeyError:
        messages.success(request, "Please login")
        return redirect("main")
    else:
        pno = request.GET.get("page_no")
        list = JobDetails.objects.all()
        p = Paginator(list, 3)
        if pno:
            pge = p.page(pno)
        else:
            pge = p.page(1)
        return render(request, "offcampusdrive.html", {"page": pge})

def walkindrive(request):
    try:
        value = request.session["email"]
    except KeyError:
        messages.success(request, "Please login")
        return redirect("main")
    else:
        pno = request.GET.get("page_no")
        list = JobDetails.objects.all()
        p = Paginator(list, 3)
        if pno:
            pge = p.page(pno)
        else:
            pge = p.page(1)
        return render(request, "walkindrive.html", {"page": pge})

def experiancejobs(request):
    try:
        value = request.session["email"]
    except KeyError:
        messages.success(request, "Please login")
        return redirect("main")
    else:
        pno = request.GET.get("page_no")
        list = JobDetails.objects.all()
        p = Paginator(list, 3)
        if pno:
            pge = p.page(pno)
        else:
            pge = p.page(1)
        return render(request, "experiancejobs.html", {"page": pge})

def passout2020(request):
    try:
        value = request.session["email"]
    except KeyError:
        messages.success(request, "Please login")
        return redirect("main")
    else:
        pno = request.GET.get("page_no")
        list = JobDetails.objects.all()
        p = Paginator(list, 3)
        if pno:
            pge = p.page(pno)
        else:
            pge = p.page(1)
        return render(request, "passout2020.html", {"page": pge})


def passout2019(request):
    try:
        value = request.session["email"]
    except KeyError:
        messages.success(request, "Please login")
        return redirect("main")
    else:
        pno = request.GET.get("page_no")
        list = JobDetails.objects.all()
        p = Paginator(list, 3)
        if pno:
            pge = p.page(pno)
        else:
            pge = p.page(1)
        return render(request, "passout2019.html", {"page": pge})

def passout2018(request):
    try:
        value = request.session["email"]
    except KeyError:
        messages.success(request, "Please login")
        return redirect("main")
    else:
        pno = request.GET.get("page_no")
        list = JobDetails.objects.all()
        p = Paginator(list, 3)
        if pno:
            pge = p.page(pno)
        else:
            pge = p.page(1)
        return render(request, "passout2018.html", {"page": pge})
# class ProfileUpdate(UpdateView):
#     model = StudentModel
#     fields = "__all__"
#     template_name = "profile.html"
#     success_url = "profile"

def forgotpassword(request):
    student = StudentForm()
    return render(request, "forgotpassword.html", {"form": student})

def updatedpassword(request):
    e = request.POST["email"]
    try:
        res=StudentModel.objects.get(email=e)
    except StudentModel.DoesNotExist:
        messages.success(request, "Please Enter valid Email or Register ")
        return redirect("main")
    else:
        res.password= request.POST["password"]
        res.save()
        messages.success(request, "PassWord Updated Succesfully, Please login")
        return redirect("main")

def logout(request):
    try:
        del request.session["email"]
    except KeyError:
        return redirect('main')
    else:
        return redirect('main')

