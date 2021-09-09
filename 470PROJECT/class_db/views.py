from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import Http404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from class_db.models import Professor
from class_db.models import ProfPreferences
from class_db.models import ProfType

from .forms import NewUserForm
from django.contrib import messages


def home(request):
    return render(request, "class_db/home.html")

def user_login(request):
    return render(request, "class_db/login.html")

def logout(request):
    return render(request, "accounts/logout")

#def schedule(request):
    #return render(request, "class_db/schedule.html")

def about(request):
    return render(request, "class_db/about.html")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("class_db/information.html")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="class_db/register.html", context={"register_form":form})

@login_required
def insertRecordProf(request):
    if request.method == 'POST':
        if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('internal_id'):
            saveRecord = Professor()
            saveRecord.fname=request.POST.get('fname')
            saveRecord.lname=request.POST.get('lname')
            saveRecord.internal_id=request.POST.get('internal_id')
            saveRecord.save()
            messages.success(request, 'Record saves successfully')
            return render(request, 'class_db/information.html')
    else:
        return render(request, 'class_db/information.html')

@login_required
def insertRecordProfPref(request):
    results = ProfType.objects.all()
    return render(request, "class_db\schedule.html",{"ProfType":results})
    if request.method == 'POST':
        if request.POST.get('pref_type') and request.POST.get('start') and request.POST.get('end'):
            saveRecord = ProfPreferences()
            saveRecord.pref_type=request.POST.get('pref_type')
            saveRecord.start=request.POST.get('start')
            saveRecord.end=request.POST.get('end')
            saveRecord.save()
            messages.success(request, 'Record saves successfully')
            return render(request, 'class_db\schedule.html')
    else:
        return render(request, 'class_db\schedule.html')
        