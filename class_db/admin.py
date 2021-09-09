from django.contrib import admin

from .models import Professor
from .models import ProfPreferences
from .models import ProfType
from .models import Professor
from .models import ProfPreferences
from .models import ProfType


from django.urls import reverse
from django.utils.http import urlencode


#Register your models here.

#admin.site.register(Professor)
admin.site.register(ProfPreferences)
#admin.site.register(ProfType)

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    
    def proftype_type_name(self, instance):
        type = instance.prof_type.id
        if(type == 1):
            return "(1) TT/T"
        elif(type == 2):
            return "(2) FTA"
        elif(type == 3):
            return "(3) PTA"
        elif(type == 4):
            return "(4) GTA"
    
    list_display = ("fname", "lname", "proftype_type_name", "internal_id")


@admin.register(ProfType)
class ProfTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "type_name", "class_hours")