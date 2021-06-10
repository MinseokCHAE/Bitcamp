'''
from common.model import DataTransferObject
from django.db import models
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django
django.setup()


class StatisticsVO(models.Model):
    police = models.TextField()
    crime = models.TextField()
    create_at = models.DateTimeField()


class StatisticsDTO(DataTransferObject):
    police = ''
    crime = ''
    create_at = ''
'''