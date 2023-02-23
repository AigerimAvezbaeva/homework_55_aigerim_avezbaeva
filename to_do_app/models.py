from django.db import models


# Create your models here.
class ToDoParagraph(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новая'),
        ('in_process', 'В процессе'),
        ('complete', 'Завершена')
    )
    title = models.CharField(max_length=400, blank=False, null=False, verbose_name='Задача')
    description = models.TextField(max_length=2000, blank=False, null=True, verbose_name='Описание задачи')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, blank=False,  default='new', verbose_name='Статус задачи')
    completion_date = models.DateField(verbose_name='Дата выполнения', blank=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.status}'

    @classmethod
    def return_choices(cls):
        statuses = dict(cls.STATUS_CHOICES)
        return statuses

