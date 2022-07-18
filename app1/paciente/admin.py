from django.contrib import admin

# Register your models here.
from paciente.models import Paciente, Antecedentes, PersonalMed

admin.site.register(Paciente)
admin.site.register(Antecedentes)
admin.site.register(PersonalMed)