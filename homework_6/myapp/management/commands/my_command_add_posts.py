from random import randint, choice

from django.core.management.base import BaseCommand
from myapp.models import Author, Posts


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        authors = Author.objects.all()

        for author in authors:
            for i in range(randint(10, 15)):
                post = Posts(name_title = f'Post № {i + 1}',
                             description= 'Some Text',
                             category=f"{choice(['документальная', 'историческая', 'политическая'])}",
                             count_watching=f'{randint(0, 1000)}',
                             is_published=f'{choice([True, False])}',
                             author=author
                             )
                post.save()


