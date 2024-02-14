from django.http import HttpResponse
from django.shortcuts import render
import logging

from web_app.models import Order

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
