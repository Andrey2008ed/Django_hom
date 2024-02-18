from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.TextField()
    date_registrated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Customer_name: {self.name}, email: {self.email},  date_registrated: {self.date_registrated}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    image = models.ImageField(
        upload_to='product_photo',  # Подпапка в MEDIA_ROOT, где будут сохраняться изображения
        verbose_name='Image',
        null=True,  # Разрешаем значение NULL в базе данных
        blank=True  # Разрешаем поле быть пустым в формах
    )

    def __str__(self):
        return f'Product: {self.name}, Price: {self.price}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order: {self.id}, Customer: {self.customer.name}, Date: {self.date_ordered}'

    def get_total_price(self):
        total = 0
        for item in self.orderitem_set.all():
            total += item.product.price * item.quantity
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'Order {self.order.id}: {self.product.name} x {self.quantity}'
