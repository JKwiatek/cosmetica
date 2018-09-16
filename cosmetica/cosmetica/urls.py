"""cosmetica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from salon_managment.views import CustomerAdd, Customers, CustomerView, HistoryAdd, SearchCustomer, BaseView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', BaseView.as_view),
    url(r'^customer_add/$', CustomerAdd.as_view(), name='customer_add'),
    url(r'^customers/$', Customers.as_view(), name='customers'),
    url(r'^customer/(?P<customer_id>(\d)+)', CustomerView.as_view(), name='customer'),
    url(r'^history_add/$', HistoryAdd.as_view(), name='history_add'),
    url(r'^search_customer/$', SearchCustomer.as_view(), name="search-customer")

]