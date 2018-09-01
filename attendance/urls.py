from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:month_num>', views.month, name='month'),
    path('signin/<int:userid>', views.signin, name='signin'),
    path('signin/new/<int:userid>', views.new, name='new'),
    path('signin/change_month/<int:userid>/<int:month_num>', views.change_month, name='change_month'),
]
