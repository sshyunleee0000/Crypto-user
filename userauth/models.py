from django.db import models

class User(models.Model):
    objects = models.Manager()
    user_no = models.AutoField(db_column='user_no', primary_key=True)
    user_id = models.CharField(db_column='user_id', max_length=255)
    user_pw = models.CharField(db_column='user_pw', max_length=5000)
    salt = models.CharField(db_column='salt', max_length=255)

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
        return "user_no : " + self.user_no