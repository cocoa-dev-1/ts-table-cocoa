from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
from TStable import settings
from . import validator

# Create your models here.

#트랜잭션 : 처리하다가 오류 나면 서이브 포인트로 반환

class Room(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def is_using():
        pass

    def get_available_time():
        pass

class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    reason = models.TextField()
    start_time = models.DateTimeField(
        help_text=_('Enter the date of start'),
        validators=[validator.min_time,validator.is_thirty_minutes],
        verbose_name=_('start date')
    )
    end_time = models.DateTimeField(
        help_text=_('Enter the date of end'),
        validators=[validator.max_time,validator.is_thirty_minutes],
        verbose_name=_('end date')
    )

    def __str__(self):
        return f'user: {self.user}\nroom: {self.room}\nresaon: {self.reason}'
