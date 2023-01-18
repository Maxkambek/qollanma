from django.db import models


class Order(models.Model):
    own_image = models.FileField(upload_to='own_images/')
    passport_image = models.FileField(upload_to='passports/')
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    date_birth = models.DateField()
    passport_data = models.CharField(max_length=15)
    price = models.PositiveBigIntegerField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.passport_data

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
