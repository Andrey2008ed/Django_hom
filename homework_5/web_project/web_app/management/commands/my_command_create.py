from django.core.management import BaseCommand

from web_app.models import Customer, Order, Product, OrderItem


class Command(BaseCommand):
    help = "Create customer, order, product."

    def handle(self, *args, **kwargs):
        for i in range(5):
            customer = Customer(name=f'Customer{i}', email=f'customer{i}@example.com', address='Road Street ',
                                phone=f'8495123445{i}')
            customer.save()

        for i in range(1, 6):
            order = Order(customer_id=f'{i}')
            order.save()

        for i in range(1, 6):
            product = Product(name=f'Product{i}', description=f'Product № {i}', price=f'{100 * i} ',
                              count=f'{2 * i}')
            product.save()

        orders = Order.objects.all()
        #
        # for order in orders:
        #
        #     order.products.set(
        #         Product.objects.all())  # Используем .set() для добавления всех продуктов к каждому заказу

        orders = Order.objects.all()
        products = Product.objects.all()

        for order in orders:
            for product in products:
                # Создаем OrderItem для каждого продукта и каждого заказа
                order_item = OrderItem(order=order, product=product, quantity=1)
                order_item.save()
