from django.urls import path
from . import views

urlpatterns = [
    path('about-me/', views.about_me_view, name='about_me'),
    path('current-time/', views.current_time_view, name='current_time'),
    path('random-quote/', views.random_quote_view, name='random_quote'),
    path('book_list/', views.book_list_view, name = 'book_list'),
    path('book_list/<int:id>', views.book_detail_view, name = 'book_detail'),
]
