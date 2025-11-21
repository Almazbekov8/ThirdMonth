from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    
    GENRE = (
        ('comedy', 'Комедия'),
        ('drama', 'Драма'),
        ('horror', 'Ужасы'),
        ('sci-fi', 'Научная фантастика'),
        ('romance', 'Романтика'),
    )
    
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50, choices = GENRE)
    pages = models.IntegerField()   
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

class Review(models.Model):
    MARK =(('1', '1 - Очень плохо'),
          ('2', '2 - Плохо'),
          ('3', '3 - Средне'),
          ('4', '4 - Хорошо'),
          ('5', '5 - Отлично'),
    )
    
    book_choice = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews', verbose_name='Книга')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    mark = models.CharField(choices=MARK, verbose_name='Оценка')
    comment = models.TextField(verbose_name='Комментарий')
    
    def __str__(self):
                return f"Отзыв от {self.user.username} - Книга: {self.book_choice.title}, Оценка: {self.mark}"
    
    
