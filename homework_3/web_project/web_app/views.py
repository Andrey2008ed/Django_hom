from datetime import timedelta
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render
import logging

from web_app.models import Order, Customer, OrderItem

logger = logging.getLogger(__name__)


def index(request):
    html = ('<h1>Добро пожаловать в интернет магазин!</h1> \
            <h3>В нашем магазине предоставлен широкий выбор ассортимента</h3> \
            <ul><li>Товары для детей</li> \
                <li>Бытовая техника</li> \
                <li>Товары для дачи</li> \
                <li>Спорт</li> \
                <li>Одежда, обувь</li> \
            </ul>')
    return HttpResponse(html)


def about(request):
    html = ('<h1>О нас</h1> \
            <p>Наш магазин предоставляет товары по лучшим ценам и высокого качества.</p> \
            <p>Магазин находится по адресу 73-й км МКАД</p> \
            <img src="https://www.hotelgreenwood.ru/upload/medialibrary/090/090999d8378bdb9fa481efb6cfb0008e.jpg" alt="Карта проезда"> \
            ')

    logger.info('Успешный вход на страницу')
    return HttpResponse(html)


def info(request, order_id):
    order = Order.objects.get(pk=order_id)
    products_list = ', '.join([f'{product.name} (Price: {product.price})' for product in order.products.all()])
    total_price = order.get_total_price()
    return HttpResponse(f'{order.customer.name} has Order{order.id}, total_sum is {total_price}:<br>.'
                        f'{products_list}<br>'
                        f'Registrated at {order.customer.date_registrated} ')


def show_customers_orders(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    orders = Order.objects.filter(customer=customer)

    orders_products = []
    for order in orders:
        # Извлекаем все данные о конкретном заказе
        order_items = OrderItem.objects.filter(order=order)

        # Товары с данными о количестве
        products_with_quantities = []
        for item in order_items:
            product = item.product
            quantity = item.quantity

            products_with_quantities.append((product, quantity))

        orders_products.append((order, products_with_quantities))

    context = {'orders_products': orders_products, 'customer': customer}
    return render(request, "web_app/customer.html", context)


def show_recent_orders(request, customer_id):
    now = timezone.now()  # получение текущего времени
    periods = {
        'week': now - timedelta(days=7),  # определение временных промежутков: за последнюю неделю
        'month': now - timedelta(days=30),
        'year': now - timedelta(days=365),
    }

    orders_data = {}
    customer = Customer.objects.get(pk=customer_id)

    for period, start_date in periods.items():
        orders_data[period] = OrderItem.objects.filter(
            order__customer=customer,      #  выбираем OrderItem объекты, где связанный Order принадлежит данному Customer
            order__date_ordered__gte=start_date   #  фильтрует OrderItem объекты, выбирая только те, дата создания заказа (date_ordered) которых больше или равна заданной начальной дате (start_date).
        ).select_related('order', 'product').order_by('-order__date_ordered')  # сортирует результаты по убыванию даты заказа, так что самые новые заказы будут первыми

    context = {
        'orders_data': orders_data,
        'customer': customer
    }
    return render(request, "web_app/recent_orders.html", context)
