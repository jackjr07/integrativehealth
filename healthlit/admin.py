from django.contrib import admin
from .models import Program, SubProgram, ConfirmedCase

admin.site.register(Program)
admin.site.register(SubProgram)
@admin.register(ConfirmedCase)
class ConfirmedCaseAdmin(admin.ModelAdmin):
    list_display = ("patName", "patProgram", "patChecked")

