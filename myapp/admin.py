from django.contrib import admin
from .models import Patient,Doctors,Transaction,Medications
from .forms import PatientForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class PatientPanel(UserAdmin):
    model = Patient
    add_form = PatientForm
    list_display = ('username', 'name', 'phone','city','age','is_active')
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Personal info', 
            {
                'fields': (
                    'name',
                    'phone',
                    'is_phone_verified',
                    'city',
                    'age',
                )
            }
        )
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','name' , 'is_active' , 'password', 'password1','phone' , 'city')}
         ),
    )
   
admin.site.register(Patient, PatientPanel)

class Customdoctor(admin.ModelAdmin):
    list_display = ('name','place','speciality_in','qualification')
admin.site.register(Doctors,Customdoctor)

class Transcationdisplay(admin.ModelAdmin):
    list_display = ('user','slot','transaction_id')
admin.site.register(Transaction,Transcationdisplay)

class Medicationsdisplay(admin.ModelAdmin):
    list_display = ('problem','medicine1','medicine2','medicine3')
admin.site.register(Medications,Medicationsdisplay)

