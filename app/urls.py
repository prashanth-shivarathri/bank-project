from django.urls import path
from . import views

urlpatterns=[
     path('',views.home,name='home'),
     path('1',views.index,name='index'),
      path("2", views.data,name="data"),
     path('3',views.edit,name='edit'),
     path('4',views.balance,name='balance'),
     path('5',views.add,name='add'),
     path('6',views.withdraw,name='withdraw'),
     path('7',views.transfer_bal,name='transfer_bal'),
]