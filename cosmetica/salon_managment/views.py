from django.shortcuts import render, redirect
from .models import Customer, CustomerHistory
from django.views import View
from salon_managment.forms import CustomerForm, HistoryForm, CustomerSearchForm


class Customers(View):

    def get(self, request):
        customers = Customer.objects.all()
        return render(request, 'customers.html', {'customers': customers})

    def post(self):
        return redirect('customer')


class CustomerAdd(View):

    def get(self, request):
        form = CustomerForm
        return render(request, 'customer_add.html', {'form': form})

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            Customer.objects.create(**form.cleaned_data)
            return redirect('customers')


class CustomerView(View):

    def get(self, request, customer_id):
        customer = Customer.objects.get(id=customer_id)
        history = CustomerHistory.objects.filter(customer=customer)

        return render(request, 'customer.html', {'customer': customer,
                                                 'history': history,
                                                 })

    def post(self, request):
        form = HistoryForm(request.POST)
        if form.is_valid():
            CustomerHistory.objects.create(**form.cleaned_data)
            return redirect('customer')


class HistoryAdd(View):

    def get(self, request):
        form = HistoryForm
        return render(request, 'history_add.html', {'form': form})

    def post(self, request):
        form = HistoryForm(request.POST)
        if form.is_valid():
            CustomerHistory.objects.create(**form.cleaned_data)
            return redirect('customers')


class SearchCustomer(View):

    def get(self, request):
        form = CustomerSearchForm
        return render(request, 'search_form.html', {'form': form})

    def post(self, request):
        form = CustomerSearchForm(request.POST)
        if form.is_valid():
            customers = Customer.objects.filter(last_name__icontains=form.cleaned_data['last_name'])
            return render(request, "customers.html", {'customers': customers})


class BaseView(View):
    def get(self, request):
        return render(request, 'base.html')