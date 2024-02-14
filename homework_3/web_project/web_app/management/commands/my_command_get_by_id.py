from django.core.management import BaseCommand
from web_app.models import Customer, Order, Product, OrderItem


class Command(BaseCommand):
    help = "Get product or customer by id."

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Product or Customer ID')

    def handle(self, *args, **kwargs):
        id = kwargs['id']

        product = Product.objects.get(id=id)
        self.stdout.write(f'{product}')

        customer = Customer.objects.get(id=id)
        self.stdout.write(f'{customer}')


