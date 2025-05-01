from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('title', max_length=50)
    anons = models.CharField('anons', max_length=250)
    text = models.TextField('text')
    date = models.DateTimeField('date')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"