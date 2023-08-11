from django.contrib import admin

from gs1.enroll.models import enroll

from enroll import enroll
# Register your models here.
@admin.register(enroll)
class Adminregistration(admin.ModelAdmin):
    list_display=('name','capital')