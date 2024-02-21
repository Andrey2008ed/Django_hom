from django.http import HttpResponse
from random import choice, randint
from django.shortcuts import render
import logging

from .form import GameForm, AuthorForm, PostForm
from .models import Coin, Author, Posts

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Succsess')
    return render(request, "myapp/index.html")


def about(request):
    logger.info('Succsess')
    return render(request, "myapp/about.html")


def game_1(request):
    answer = choice(['Орел', 'Решка'])
    # coin = Coin(side=answer)
    # coin.save()
    #
    # logger.info(f'Answer is {answer}')

    context = {"result": answer}
    return render(request, "myapp/games.html", context)


def static_game(request):
    count = Coin.count_throw()
    return HttpResponse(f"Орел: {count['Орел']}, Решка: {count['Решка']}")


def full_name(request):
    full_name = Author.objects.all()
    result = ''
    for item in full_name:
        result += f'{item.full_name()}<br>'

    return HttpResponse(result)


def game_2(request):
    answer = randint(1, 6)
    logger.info(f'Ответ равен {answer}')
    context = {"result": answer}
    return render(request, "myapp/games.html", context)


def game_3(request):
    answer = randint(0, 100)
    logger.info(f'Ответ равен {answer}')
    context = {"result": answer}
    return render(request, "myapp/games.html", context)


def show_posts(request, author_id):
    author = Author.objects.get(pk=author_id)
    posts = Posts.objects.filter(author=author)
    context = {'posts': posts}
    return render(request, "myapp/posts.html", context)


def show_post_id(request, post_id):
    post = Posts.objects.get(pk=post_id)
    context = {'post': post}
    return render(request, "myapp/post.html", context)


def choice_games(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.data['game']
            number = form.data['number']
            if game == 'К':
                return game_2(request)
            elif game == 'М':
                return game_1(request)
            elif game == 'Ч':
                return game_3(request)
    else:
        form = GameForm()

    return render(request, "myapp/games_form.html", {'form': form})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            name = form.data['name']
            surname = form.data['surname']
            email = form.data['email']
            biography = form.data['biography']
            birthday = form.data['birthday']
            author = Author(name=name, surname=surname, email=email, biography=biography, birthday=birthday)
            author.save()
    else:
        form = AuthorForm()
    return render(request, "myapp/add_author.html", {'form': form})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            name_title = form.data['name_title']
            description = form.data['description']
            author_id = form.data['author']
            author = Author.objects.get(pk=author_id)
            category = form.data['category']
            count_watching = form.data['count_watching']

            post = Posts(name_title=name_title, description=description,
                         author=author, category=category,
                         count_watching=count_watching)
            post.save()
    else:
        form = PostForm()
    return render(request, "myapp/add_post.html", {'form': form})
