from django.shortcuts import render,redirect
from .models import Product, Purchase
from .utils import get_simple_plot
from .forms import PurchaseForm
import pandas as pd
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def sales_dist_view(request):
    df=pd.DataFrame(Purchase.objects.all().values())
    print(df)
    return HttpResponse("hello salesman")

@login_required
def chart_select_view(request):
    graph=None
    error_message=None
    df=None
    price=None

    try:
        product_df=pd.DataFrame(Product.objects.all().values())
        purchase_df=pd.DataFrame(Purchase.objects.all().values())
        product_df['product_id']=product_df['id']
    except:
        product_df=None
        purchase_df=None

    
    if request.method=="POST":
        chart_type=request.POST['sales']
        date_from=request.POST['date_from']
        date_to=request.POST['date_to']
        
    
    
    context={'products':product_df.to_html(),
    
    }

    
  
    return render(request,'products/main.html',context)
@login_required
def add_purchase_view(request):
    form = PurchaseForm()
    context={
        'form':form,
    }
    return render(request,'products/add.html',context)