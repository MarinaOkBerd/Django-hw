from django.core.management.base import BaseCommand
from hw2.models import Customer



class Command(BaseCommand):
    help = "Get customer"

    def handle(self, *args, **kwargs):
        from django_hw.hw2.models import Customer
        customer = Customer(name='Marina', email='marina@mail.ru', phone='81234567899',
                            address='S-Petersburg st.Zavodskaya 1 99')
        customer.save()
        self.stdout.write(f'{customer}')