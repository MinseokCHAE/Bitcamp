from django.db import models


class Member(models.Model):
    userid = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=12)
    email = models.TextField()

    class Meta:
        managed = True
        db_table = 'member'
