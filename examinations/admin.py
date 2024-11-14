from django.contrib import admin

from .models import Examination


@admin.register(Examination)
class ExaminationAdmin(admin.ModelAdmin):
    pass