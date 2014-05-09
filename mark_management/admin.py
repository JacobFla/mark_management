from django.contrib import admin
from mark_management.models import Subject, Typ, Mark, Semester, Year

admin.site.register(Semester)

from django.contrib import admin
from mark_management.models import Mark

class MarkAdmin(admin.ModelAdmin):
    list_display = ['date', 'value', 'topic', 'typ', 'semester', 'subject']

admin.site.register(Mark, MarkAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher', 'year', 'get_typs']

admin.site.register(Subject, SubjectAdmin)

class TypAdmin(admin.ModelAdmin):
    list_display = ['name', 'valence']

admin.site.register(Typ, TypAdmin)

class YearAdmin(admin.ModelAdmin):
    list_display = ['name', 'semester_1', 'semester_2', 'marks_interval_min', 'marks_interval_max']

admin.site.register(Year, YearAdmin)