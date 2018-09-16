from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=128, verbose_name='Imię')
    last_name = models.CharField(max_length=128, verbose_name='Nazwisko')
    phone = models.IntegerField(verbose_name='Numer telefonu')

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class CustomerHistory(models.Model):
    customer = models.ForeignKey(Customer, on_delete="CASCADE")
    content = models.TextField()

