from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:month_num>', views.month, name='month'),
    path('signin/<int:userid>', views.signin, name='signin'),
]
