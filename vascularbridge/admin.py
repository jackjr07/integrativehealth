from django.contrib import admin
from .models import limbIndexSym, limbIndexRutherford, limbIndexDiagnosis, limbSurgicalPlan, limbNonSurgicalPlan

admin.site.register(limbIndexSym)
admin.site.register(limbIndexRutherford)
admin.site.register(limbIndexDiagnosis)
admin.site.register(limbSurgicalPlan)
admin.site.register(limbNonSurgicalPlan)
