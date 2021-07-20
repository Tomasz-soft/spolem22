from django.db import models

# Create your models here.
from towary.models import Towary


class Nag_rach(models.Model):
    status = models.IntegerField()
    id_nagrach = models.IntegerField(primary_key=True,)
    numer_rach = models.IntegerField(unique=True)
    data_operacji = models.DateField()
    od_dnia = models.DateField()
    do_dnia = models.DateField()
    uwagi = models.CharField(max_length=70)
    typ_rach = models.CharField(max_length=20)
    stat_prom = models.IntegerField()
    attr_rach = models.IntegerField()
    stat_prom = models.IntegerField()
    user_id = models.IntegerField()
    id_ref_nagrach = models.IntegerField()

    def __str__(self):
        return self.uwagi + ' Początek:' + self.od_dnia.strftime("%Y-%m-%d") + ' Koniec:' + self.do_dnia.strftime("%Y-%m-%d")

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "naglowki_rach"
        managed = False


class Poz_rach(models.Model):
    status = models.IntegerField()
    id_pozrach = models.IntegerField(db_column='id_pozrach', primary_key=True)
    id_nagrach = models.ForeignKey(
        Nag_rach, db_column='id_nagrach', on_delete=models.CASCADE)
    # id_prom = models.IntegerField()
    id_tow = models.ForeignKey(
        Towary, db_column='id_tow', on_delete=models.CASCADE)
    # id_tow = models.IntegerField()
    stara_cena = models.IntegerField()
    nowa_cena = models.IntegerField()
    bazowa_cena = models.IntegerField()
    cena_po_prom = models.IntegerField()
    cena_zakupu = models.IntegerField()
    ilosc_prog = models.IntegerField()
    atribs_tow = models.IntegerField()

    class Meta:
        db_table = "pozycje_rach"
        managed = False
