from django.db import models
# Create your models here.
class Contact(models.Model):
    LANGUAGE_CHOICES = (
    ('English','English'),
    ('Hindi', 'Hindi'),
    ('Telugu','Telugu'),
    ('Malyalam','Malyalam'),
    ('French','French'),
    )
    GENRE_CHOICES = (
        ('NonFiction','Nonfiction'),
        ('Fiction','Fiction'),
        ('Satire','Satire'),
        ('Classic','Classic'),
        ('Adventure','Adventure'),
    )

    bookname = models.CharField(max_length=200, default='book')
    author = models.CharField(max_length=200, default='author')
    language = models.CharField(max_length=200,choices=LANGUAGE_CHOICES, default='English')
    genre = models.CharField(max_length=200,choices=GENRE_CHOICES, default='Fiction')
    def __str__(self):
        return self.bookname