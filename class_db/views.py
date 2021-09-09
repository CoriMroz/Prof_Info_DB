from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from class_db.models import Professor
from class_db.models import ProfPreferences
from class_db.models import ProfType


from django.contrib import messages


def home(request):
    return render(request, "class_db/home.html")

#def signup(request):
   #return render(request, "class_db/signup.html")

def login(request):
    return render(request, "class_db/login.html")

#def schedule(request):
    #return render(request, "class_db/schedule.html")


def insertRecordProf(request):
    if request.method == 'POST':
        if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('internal_id'):
            saveRecord = Professor()
            saveRecord.fname=request.POST.get('fname')
            saveRecord.lname=request.POST.get('lname')
            saveRecord.internal_id=request.POST.get('internal_id')
            saveRecord.save()
            messages.success(request, 'Record saves successfully')
            return render(request, 'class_db\signup.html')
    else:
        return render(request, 'class_db\signup.html')

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
        