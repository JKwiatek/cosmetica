from django import forms
from .models import Customer, CustomerHistory


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'


class HistoryForm(forms.ModelForm):

    class Meta:
        model = CustomerHistory
        fields = '__all__'


class CustomerSearchForm(forms.Form):
    last_name = forms.CharField(label='Nazwisko', max_length=128)