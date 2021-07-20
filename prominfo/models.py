from promocje.models import Promocje
from promcent.models import Nag_rach, Poz_rach
from django.db import models

# Create your models here.
#from sklepy.models import Sklepy
#from pracownicy.models import Pracownicy


class PromCentInfo(models.Model):
    datazak_od = models.DateField()
    datazak_do = models.DateField()
    uwagi = models.CharField(max_length=250, blank=True)
    nr_prom = models.OneToOneField(
        Nag_rach, to_field='numer_rach', db_column='nr_prom', related_name='NagRach', on_delete=models.CASCADE, unique=True)
    id_prac = models.IntegerField()
    nazwa_prom = models.CharField(max_length=70)

    class Meta:
        db_table = 'promcent_informacje'
        managed = False

    def __str__(self):
        return self.uwagi


class PromCentInfoOnly(models.Model):
    datazak_od = models.DateField()
    datazak_do = models.DateField()
    uwagi = models.CharField(max_length=250)
    # nr_prom = models.OneToOneField(
    #   Nag_rach, to_field='numer_rach', db_column='nr_prom', related_name='NagRach', on_delete=models.CASCADE)
    nr_prom = models.IntegerField(unique=True)
    id_prac = models.IntegerField()
    nazwa_prom = models.CharField(max_length=70)

    class Meta:
        db_table = 'promcent_informacje'
        managed = False

    def __str__(self):
        return self.uwagi
