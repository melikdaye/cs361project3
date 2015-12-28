from django.contrib import admin

# Register your models here.
from formapp.models import teachers, students, courses

admin.site.register(teachers)
admin.site.register(students)
admin.site.register(courses)