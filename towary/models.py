from django.db import models

# Create your models here


class Towary(models.Model):
    status = models.IntegerField()
    id_tow = models.IntegerField(primary_key=True)
    id_gtow = models.IntegerField()
    id_dtow = models.IntegerField()
    id_branz = models.IntegerField()
    atribs_tow = models.IntegerField()
    naz_kas_tow = models.CharField(blank=False, max_length=25)
    nazwa_tow = models.CharField(blank=False, max_length=40)
    ident_tow = models.CharField(max_length=13)
    bar_kod_tow = models.CharField(max_length=13, blank=False)
    gr_rabat_t = models.IntegerField()
    cena_d_tow = models.IntegerField()

    def __str__(self):
        return self.bar_kod_tow + " " + self.nazwa_tow

    class Meta:
        db_table = "towary"
        managed = False
