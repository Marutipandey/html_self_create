from django.urls import URLPattern, path
from .views import chart_select_view,add_purchase_view,sales_dist_view
app_name='products'

urlpatterns=[
    path('',chart_select_view,name="main-products-view"),
    path('add/',chart_select_view,name="add-purchase-view"),
    path('sales/',chart_select_view,name="sales-view"),

]
