from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    # кастомная модель пользователя
    # username - уже созданно в абстрактном пользователе
    # password - уже созданно в абстрактном пользователе
    # Добавим опциональные поля
    #спец поле для почты EmailField 
    email = models.EmailField(unique=True, null=False)
    # поле для большого количество текста(str)
    description = models.TextField()
    # Поле дл символ опр количества с ограничением максимум 255
    phone = models.CharField(max_length=11, unique=True, blank=True, null=True)
    # 2 вида поле для картинки
    avatar = models.ImageField(upload_to='avatars/')
    # Если вы храните не у себя в сервере картинку
    # храните их на удаленке или даеие пользователю загрузить аву по ссылке
    image = models.URLField()

    # добавляет флажо аутф группы людей
    # и так же задаем related name для избежения конфликтов
    groups = models.ManyToManyField('auth.Group',related_name='custom_user',blank=True)

    def __str__(self):
        return self.username