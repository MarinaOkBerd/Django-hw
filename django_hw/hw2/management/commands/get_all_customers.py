from django.core.management.base import BaseCommand

from hw2.models import Customer


class Command(BaseCommand):
    help = "Get all customers"

    def handle(self, *args, **kwargs):
        customer = Customer.objects.all()
        self.stdout.write(f'{customer}')