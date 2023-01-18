from django.db import models


class Useful(models.Model):
    title = models.CharField(max_length=222, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Полезная информация'
        verbose_name_plural = 'Полезная информация'


class Offer(models.Model):
    name = models.CharField(max_length=221, verbose_name='название')
    subtitle = models.CharField(max_length=221, verbose_name='подзаголовок')
    date = models.CharField(max_length=100, verbose_name='Дата')
    price = models.PositiveIntegerField(verbose_name='цена')
    price_dollar = models.PositiveIntegerField(verbose_name='доллар')
    image = models.ImageField(upload_to='offers/', verbose_name='изображение')
    created_at = models.DateField()

    @property
    def get_dollar(self):
        return self.price / 11000

    class Meta:
        verbose_name = 'Специальные предложения'
        verbose_name_plural = 'Специальные предложения'


class News(models.Model):
    title = models.CharField(max_length=333, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержание')
    image = models.ImageField(upload_to='news/', verbose_name='изображение')
    created_at = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


class Contact(models.Model):
    name = models.CharField(max_length=221)
    phone = models.CharField(max_length=18)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'


class Feedback(models.Model):
    message = models.TextField()

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзыв'
