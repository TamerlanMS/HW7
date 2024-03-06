from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError


def positive_number_validator(value):
    if value < 0:
        raise ValidationError("Value must be a positive number.")


class Todo(models.Model):
    class Status(models.TextChoices):
        CREATED = 'c', 'created'
        IN_PROGRESS = 'i', 'in progress'
        DONE = 'd', 'completed'
        
    title = models.CharField(max_length=255, 
                             validators=[validators.MinLengthValidator(5, "Title must be greater than 5 characters")], verbose_name='Заголовок')
    body = models.TextField(validators=[validators.MaxLengthValidator(255, "Body must be less than 255 characters"), validators.MinLengthValidator(20, "Body must be greater than 20 characters")], verbose_name='Описание')
    deadline = models.DateField(verbose_name='Дедлайн')
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.CREATED, verbose_name='Статус')
    
    some_field = models.IntegerField(validators=[positive_number_validator])
       
    def __str__(self):
        return self.title
    
    def get_id_and_title(self):
        return f"{self.id}: {self.title}"

    def get_total_length(self):
        return len(self.title) + len(self.body)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title
        