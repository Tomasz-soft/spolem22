from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
from towary.models import Towary


class PromocjaCzas(models.Model):
    status = models.IntegerField()
    id_pczas = models.IntegerField(primary_key=True, unique=True)
    godz_prom = models.IntegerField()
    dt_prom = models.IntegerField()
    mr_prom = models.IntegerField()
    data_p_od = models.DateField()
    data_p_do = models.DateField()
    nr_prom = models.IntegerField(unique=True)
    nazwa_prom = models.CharField(max_length=40)
    nr_rabat_k = models.IntegerField()
    typ_prom = models.IntegerField()
    uwagi_prom = models.CharField(max_length=70)
    data_mod = models.DateTimeField()
    user_id = models.IntegerField()
    kwota_prog = models.IntegerField()
    max_prom = models.IntegerField()

    class Meta:
        db_table = 'promocja_czas'
        managed = False


class PromocjaCzas_pozycja(models.Model):

    id_pczasp = models.IntegerField(primary_key=True)
    status = models.IntegerField()
    id_prom_czas = models.ForeignKey(
        PromocjaCzas, db_column='id_prom_czas',to_field='id_pczas', on_delete=models.CASCADE)
    id_tow = models.ForeignKey(
        Towary, db_column='id_tow', on_delete=models.CASCADE)
    rabat = models.IntegerField()
    nr_poz = models.IntegerField()
    attr_prom = models.IntegerField()
    ilosc_prom = models.IntegerField()
    kwota_rab = models.IntegerField()
    cena_d_prom = models.IntegerField()
    ilosc_plat = models.IntegerField()
    ilosc_pkt = models.IntegerField()
    przelicz = models.IntegerField()

    class Meta:
        db_table = 'promocja_czas_pozycja'
        managed = False
