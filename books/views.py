from django.shortcuts import render
from django.http import HttpResponse

def about_me_view(request):
    if request.method == 'GET':
        return HttpResponse(f"Меня зовут Азирет, мне 18 лет." 
                            "Я изучаю программирование и стремлюсь стать отличным разработчиком.")
        