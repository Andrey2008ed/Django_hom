from django.core.management import BaseCommand
from web_app.models import Customer, Order, Product, OrderItem


class Command(BaseCommand):
    help = "Delete Customer by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        customer = Customer.objects.filter(pk=pk).first()
        if customer is not None:
            customer.delete()
            self.stdout.write(f'{customer}')
