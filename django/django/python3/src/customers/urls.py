from django.urls import URLPattern, path

app_name='csvs'
from .views import customer_corr_view

urlpatterns=[
    path('',customer_corr_view,name='main-customers-view'),
    ]
