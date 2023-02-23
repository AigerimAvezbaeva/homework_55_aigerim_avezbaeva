from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


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
    is_deleted = models.BooleanField(verbose_name='Удалено', null=False, default=False)
    deleted_at = models.DateTimeField(verbose_name='Дата и время удаления', null=True, default=None)
    updated_at = models.DateField(auto_now=True, verbose_name="Дата и время обновления")


    def __str__(self):
        return f'{self.title} - {self.status}'

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длиннее 2 символов')
        return title

