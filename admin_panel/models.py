from django.db import models
from django.contrib.auth.models import User



class PlasticWindowsCategories(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Пластиковые окна Категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категории пластиковых окон"
        verbose_name_plural = "Категории пластиковых окон"



class PlasticWindowsGetCategories(models.Model):
    plastic_windows_cateories = models.ForeignKey(
        PlasticWindowsCategories,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    title = models.CharField(
        max_length=300,
        null=True, blank=True,
        verbose_name='Заголовок'
    )
    content_one = models.CharField(
        max_length=300,
        null=True, blank=True,
        verbose_name='Контент один'
    )
    content_two = models.CharField(
        max_length=300,
        null=True, blank=True,
        verbose_name='Контент второе'
    )
    content_three = models.CharField(
        max_length=300,
        null=True, blank=True,
        verbose_name='Контент третий'
    )
    content_four = models.CharField(
        max_length=300,
        null=True, blank=True,
        verbose_name='Контент четвертый'
    )
    background = models.ImageField(
        upload_to='background/',
        null=True, blank=True,
        verbose_name='Изображение на заднем плане'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пластиковые окна Получить категории"
        verbose_name_plural = "Пластиковые окна Получить категории"

class Contacts(models.Model):
    full_name = models.CharField(
        max_length=300,
        null=True, blank=True,
        verbose_name='Полное имя'
    )
    number = models.IntegerField(
        default=0,
        null=True,
        blank=True,
        verbose_name='Номер телефона'
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

class Windows(models.Model):
    background = models.ImageField(
        upload_to='background/',
        null=True, blank=True,
        verbose_name='Изображение на заднем плане'
    )
    title = models.CharField(
        max_length=300,
        null=True, blank=True,
        verbose_name='Заголовок'
    )
    content = models.CharField(
        max_length=300,
        null=True, blank=True,
        verbose_name='Контент'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Окна"
        verbose_name_plural = "Окна"

class WindowsImages(models.Model):
    windows = models.ForeignKey(
        Windows,
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name='Идентификатор Окно',
        related_name='windows_id'
    )
    background = models.ImageField(
        upload_to='background/',
        null=True, blank=True,
        verbose_name='Изображение на заднем плане'
    )

    def __str__(self):
        return self.windows.title

    class Meta:
        verbose_name = "Образы Windows"
        verbose_name_plural = "Образы Windows"

class OurWork(models.Model):
    country = models.CharField(
        max_length=300,
        null=True, blank=True,
        verbose_name='Страна'
    )
    background = models.ImageField(
        upload_to='background/',
        null=True, blank=True,
        verbose_name='Изображение на заднем плане'
    )

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = "Наша работа"
        verbose_name_plural = "Наша работа"

class OurServices(models.Model):
    name = models.CharField(
        max_length=300,
        null=True, blank=True,
        verbose_name='Наименование услуги'
    )
    background = models.ImageField(
        upload_to='background/',
        null=True, blank=True,
        verbose_name='Изображение на заднем плане'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Наши услуги"
        verbose_name_plural = "Наши услуги"

class OurServiceGet(models.Model):
    ourservices = models.ForeignKey(
        OurServices,
        on_delete=models.CASCADE,
        verbose_name='',
        null=True, blank=True
    )
    background = models.ImageField(
        upload_to='background/',
        null=True, blank=True,
        verbose_name='Изображение на заднем плане'
    )
    content = models.CharField(
        max_length=300,
        null=True, blank=True,
        verbose_name='Контент'
    )

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Получите наши услуги"
        verbose_name_plural = "Получите наши услуги"

class Plastics(models.Model):
    name = models.CharField(
        max_length=300,
        null=True, blank=True,
        verbose_name='Полное имя'
    )
    image = models.ImageField(
        upload_to='plastic',
        null=True, blank=True,
        verbose_name=''
    )

    class Meta:
        verbose_name = "Пластмассы"
        verbose_name_plural = "Пластмассы"