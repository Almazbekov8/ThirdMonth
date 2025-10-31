from django.shortcuts import render
from django.http import HttpResponse

def about_me_view(request):
    if request.method == 'GET':
        return HttpResponse(f"Меня зовут Азирет, мне 18 лет." 
                            "Я изучаю программирование и стремлюсь стать отличным разработчиком.")
        
def current_time(request):
    if request.method == 'GET':
        time_str = "12:00"
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
    
    