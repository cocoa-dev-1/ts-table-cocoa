from django.db import models

# Create your models here.
'''
    ToDo
    방의 이름, 방의 크기
'''

class Room(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def is_using():
        pass

    def get_available_time():
        pass
    