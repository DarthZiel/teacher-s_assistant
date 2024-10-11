from django.db import models
from django.conf import settings
# Create your models here.

from django.db import models

class Ward(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=100, verbose_name="Отчество", blank=True, null=True)
    ward_class = models.CharField(max_length=50, verbose_name="Класс")
    address = models.TextField(verbose_name="Адрес")
    teacher_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}".strip()
