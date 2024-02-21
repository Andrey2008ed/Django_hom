from datetime import datetime

from django.contrib import admin

from .models import Coin, Author, Posts


class AuthorAdmin(admin.ModelAdmin):
    @admin.action(description="Изменение даты рождения")
    def reset_birthday(modeladmin, request, queryset):
        queryset.update(birthday=datetime.now())

    list_display = ['name', 'surname', 'email', 'biography', 'birthday']
    search_fields = ['name']
    ordering = ['-birthday']
    list_filter = ['name']
    actions = [reset_birthday]
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
                'description': 'Почта и биография автора',
                'fields': ['email', 'biography'],
        },
        ),

        (
            'Дата рождения',
            {
                'description': 'Дата рождения',
                'fields': ['birthday'],
            }
        ),
    ]


admin.site.register(Coin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Posts)
