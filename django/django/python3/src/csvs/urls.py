from django.urls import URLPattern, path

app_name='csvs'
from .views import upload_file_view

urlpatterns=[
    path('',upload_file_view,name="upload-view"),
    ]
