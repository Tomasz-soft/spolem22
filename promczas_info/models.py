from django.db import models
from promczas_cent.models import PromocjaCzas, PromocjaCzas_pozycja
# Create your models here.


class PromCzasInfo(models.Model):
    #status = models.IntegerField()
    datazak_od = models.DateField()
    datazak_do = models.DateField()
    uwagi = models.CharField(max_length=250)
    nr_prom = models.OneToOneField(
        PromocjaCzas, to_field='nr_prom', db_column='nr_prom', related_name='PromCzas', on_delete=models.CASCADE)
    id_prac = models.IntegerField()
    #id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'promczas_informacje'
        managed = False

    def __str__(self):
        return self.uwagi


class PromCzasInfoOnly(models.Model):
    #status = models.IntegerField()
    datazak_od = models.DateField()
    datazak_do = models.DateField()
    uwagi = models.CharField(max_length=250)
    nr_prom = models.IntegerField(unique=True)
    id_prac = models.IntegerField()
    #id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'promczas_informacje'
        managed = False

    def __str__(self):
        return self.uwagi
