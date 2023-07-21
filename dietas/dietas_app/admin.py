from django.contrib import admin
from .models import Paciente


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome','telefone','email')


admin.site.register(Paciente, PacienteAdmin)
