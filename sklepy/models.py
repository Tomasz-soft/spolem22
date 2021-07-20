
from django.db import models

# Create your models here.
from promcent.models import Nag_rach


class Sklepy(models.Model):

    db_id = models.IntegerField(primary_key=True)
    db_name = models.CharField(max_length=64)
    db_ident = models.CharField(max_length=20)
    archive = models.BooleanField(default=True)

    def __str__(self):
        return 'schema: ' + self.db_name + 'identyfikator:' + self.db_ident

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "databases"
        managed = False


class BazyRach(models.Model):
    id_dbrach = models.IntegerField(db_column='id_dbrach', primary_key=True)
    status = models.IntegerField()
    db_id = models.ForeignKey(
        Sklepy, db_column='db_id', on_delete=models.CASCADE)
    id_nagrach = models.ForeignKey(
        Nag_rach, db_column='id_nagrach', on_delete=models.CASCADE)
    data_operacji = models.DateTimeField()
    nr_kontr = models.IntegerField()

    class Meta:
        db_table = 'bazy_rach'
        managed = False
