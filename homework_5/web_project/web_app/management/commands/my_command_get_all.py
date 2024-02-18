from django.core.management import BaseCommand
from web_app.models import Customer, Order, Product, OrderItem


class Command(BaseCommand):
    help = "Get all customers, orders."

    def handle(self, *args, **kwargs):
        customers = Customer.objects.all()
        self.stdout.write(f'{customers}')

        orders = Order.objects.all()
        self.stdout.write(f'{orders}')
