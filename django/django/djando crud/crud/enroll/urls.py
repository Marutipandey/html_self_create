from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='enroll.index'),
    path('/create', views.create, name='enroll.create'),
    path('/store', views.store, name='enroll.store'),
    path('/view/<int:id>', views.view, name='enroll.view'),
    path('/delete/<int:id>', views.delete, name='enroll.delete'),
    path('/edit/<int:id>', views.edit, name='enroll.edit'),
    path('/update/<int:id>', views.update, name='enroll.update'),
]