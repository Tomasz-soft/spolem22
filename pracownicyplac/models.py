from django.db import models
from django.db import models
from django.db.models.deletion import CASCADE
from sklepy.models import Sklepy
from pracownicy.models import Pracownicy
# Create your models here.


class PracownicyPlac(models.Model):
    id_pracp = models.IntegerField(primary_key=True)
    status = models.IntegerField()
    db_id = models.ForeignKey(Sklepy, db_column='db_id', on_delete=CASCADE)
    #id_prac = models.IntegerField(unique=True)
    id_prac = models.ForeignKey(
        Pracownicy,  db_column='id_prac', unique=True, related_name='PracPlac', on_delete=CASCADE)

    class Meta:
        db_table = 'pracownicy_plac'
        managed = False
