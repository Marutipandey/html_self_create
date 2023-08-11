from django.contrib import admin

from .models import Employee,job
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','gender','joining_data']


@admin.register(job)
class jobAdmin(admin.ModelAdmin):
    list_display=['name']
