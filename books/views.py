from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models
import random
from django.db.models import Avg

def about_me_view(request):
    if request.method == 'GET':
        return HttpResponse(f"Меня зовут Азирет, мне 18 лет." 
                            "Я изучаю программирование и стремлюсь стать отличным разработчиком.")
        
def current_time_view(request):
    if request.method == 'GET':
        
        now = datetime.now()
        time_str = now.strftime("%H:%M")
        hours, minutes = map(int, time_str.split(":"))
        
        if hours < 12:
            message = "Сейчас утро"
        elif 12 <= hours < 15:
            message = "Сейчас обед"
        elif 15 <= hours < 21:
            message = "Сейчас вечер"
        else:
            message = "Сейчас ночь"

        return HttpResponse(f"Время: {time_str}. {message}")

def random_quote_view(request):
    quotes = [
        "«Не так страшен враг, как равнодушие друзей.» — Виктор Гюго",
        "«Быть можно дельным человеком и думать о красе ногтей.» — Александр Пушкин",
        "«Человек рожден для счастья, как птица для полета.» — Антон Чехов",
        "«Свобода ничего не стоит, если она не включает в себя свободу ошибаться.» — Махатма Ганди",
        "«Счастье — это когда то, что ты думаешь, говоришь и делаешь, находится в гармонии.» — Лев Толстой",
    ]
    phrase = random.choice(quotes)
    return HttpResponse(phrase)

def book_list_view(request):
    if request.method == 'GET':
        book = models.Book.objects.all()
        context = {
            'book': book
        }
        return render(request, template_name ='books/books.html', context=context)

def book_detail_view(request, id):
    if request.method == 'GET':
        book = get_object_or_404(models.Book, id=id)
        avg_rating = book.reviews.aggregate(Avg('mark'))['mark__avg']
        
        context = {
            'book': book,
            'avg_rating': avg_rating
        }
        return render(request, template_name='books/book_detail.html', context=context)


    
    