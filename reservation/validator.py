import datetime
from dateutil.parser import parse
from django.core.exceptions import ValidationError

def min_time(value):
    if value.hour < 9:
        raise ValidationError('오전 9시보다 일찍 등록할 수 없습니다.')

def max_time(value):
    if value.hour > 22:
        raise ValidationError('오후 10시 이후로는 등록할 수 없습니다.')

def is_thirty_minutes(value):
    if value.minute / 30 != 0:
        raise ValidationError('30분 단위로만 예약이 가능합니다.')