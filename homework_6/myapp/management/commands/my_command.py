from django.core.management.base import BaseCommand
from myapp.models import Author

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for i in range(1, 10):
            author = Author(name=f'name{i}',
                            surname=f'surname{i}',
                            email=f'user{i}@mail.com',
                            biography='Моя биография',
                            birthday=f'2000-01-0{i}')
            author.save()
