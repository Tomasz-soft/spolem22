from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
from sklepy.models import Sklepy
#from pracownicyplac.models import PracownicyPlac


class Pracownicy(models.Model):

    # id_prac = models.ForeignKey(PracownicyPlac, unique=True, to_field='id_prac',
    #                            db_column='id_prac', primary_key=True, on_delete=CASCADE)
    id_prac = models.IntegerField(
        unique=True, primary_key=True, db_column='id_prac')
    status = models.IntegerField()
    nazw_prac = models.CharField(max_length=30)
    imie_prac = models.CharField(max_length=20)
    ident_prac = models.CharField(max_length=13)
    haslo_prac = models.CharField(max_length=88)
    attr_prac = models.IntegerField()
    klucz_prac = models.CharField(max_length=13)
    user_id = models.IntegerField()

    # def __str__(self):
    #     return self.nazw_prac + ' ' + self.imie_prac

    class Meta:
        db_table = 'pracownicy'
        managed = False
