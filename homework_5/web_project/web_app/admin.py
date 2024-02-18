from django.contrib import admin

from web_app.models import Product, Customer, Order


class CustomerAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'phone', 'address', 'date_registrated']
    search_fields = ['name']
    ordering = ['-date_registrated']
    list_filter = ['address','email']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Данные о контактах покупателя',
                'fields': ['email', 'phone' ]
            },
        ),

        (
            'Адрес',
            {
                'description': 'Адрес',
                'fields': ['address'],
            }
        ),
    ]


class ProductAdmin(admin.ModelAdmin):
    @admin.action(description="Обнуление количества продукта")
    def reset_count(modeladmin, request, queryset):
        queryset.update(count=0)

    list_display = ['name', 'description', 'price', 'count']
    search_fields = ['name']
    ordering = ['-price']
    list_filter = ['name']
    actions = [reset_count]

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Данные о продукте',
                'fields': ['description', 'price']
            },
        ),

        (
            'Количество товара',
            {
                'description': 'Количество',
                'fields': ['count'],
            }
        ),
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order)
