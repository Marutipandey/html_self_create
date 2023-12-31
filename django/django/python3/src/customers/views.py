from django.shortcuts import render
import pandas as pd
# Create your views here.
import matplotlib.pyplot as plt
import seaborn as sns
from .models import Customer
from  products.utils import get_image
from django.contrib.auth.decorators import login_required

@login_required
def customer_corr_view(request):
    df=pd.DataFrame(Customer.objects.all().values())
    corr=round(df['budget'].corr(df['employment']),2)

    plt.switch_backend('Agg')
    sns.jointplot(x='budget',y='employment',kind='reg',data=df).set_axis_labels('Company budget','No of employees')
    graph=get_image()
    context={
        'graph':graph,
        'corr':corr,
    }

    return render(request,'customers/main.html',context)