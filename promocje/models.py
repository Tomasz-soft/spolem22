#from prominfo.models import PromCentInfo
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
from towary.models import Towary
#from sklepy.models import Sklepy
#from pracownicy.models import Pracownicy

# Create your models here.


class Promocje(models.Model):
    status = models.IntegerField()
    nazwa_prom = models.CharField(max_length=25)
    id_prom = models.IntegerField(primary_key=True)
    data_d_prom = models.DateTimeField()
    data_b_prom = models.DateTimeField()
    data_e_prom = models.DateTimeField()
    id_b_prac = models.IntegerField()
    id_e_prac = models.IntegerField()
    uwagi_prom = models.CharField(max_length=70)
    nr_prom = models.IntegerField(unique=True)
    stat_prom = models.IntegerField()

    def __str__(self):
        return self.uwagi_prom + ' Początek:' + self.data_b_prom.strftime("%Y-%m-%d") + ' Koniec:' + self.data_e_prom.strftime("%Y-%m-%d")

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "promocje"
        managed = False


class PozProm(models.Model):
    status = models.IntegerField()
    id_pprom = models.IntegerField(primary_key=True)
    id_prom = models.ForeignKey(
        Promocje, db_column='id_prom', on_delete=models.CASCADE)
    # id_prom = models.IntegerField()
    id_tow = models.ForeignKey(
        Towary, db_column='id_tow', on_delete=models.CASCADE)
    # id_tow = models.IntegerField()
    cena_d_old = models.IntegerField()
    cena_d_prom = models.IntegerField()
    ilosc_prom = models.IntegerField()
    obrot_prom = models.IntegerField()
    id_knt = models.IntegerField()
    data_b_prom = models.DateTimeField()
    data_e_prom = models.DateTimeField()
    stat_prom = models.IntegerField()
    cena_zakupu = models.IntegerField()
    ilosc_prog = models.IntegerField()

    class Meta:
        db_table = "poz_prom"
        managed = False
