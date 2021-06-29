from django.db import models


class Member(models.Model):
    userid = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=12)
    email = models.TextField()

    class Meta:
        managed = True
        db_table = 'member'

    def __str__(self):
        return f'[{self.pk} is userid = {self.userid},' \
               f' password = {self.password}' \
               f' name = {self.name} ' \
               f' email = {self.email} '
