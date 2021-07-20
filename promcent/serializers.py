from rest_framework import serializers
from promcent.models import Nag_rach, Poz_rach


class PromCentSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    id_prom = serializers.IntegerField()
    data_d_prom = serializers.DateField()
    data_b_prom = serializers.DateField()
    data_e_prom = serializers.DateField()
    uwagi_prom = serializers.CharField()
    nr_prom = serializers.IntegerField()
    stat_prom = serializers.IntegerField()
    datazak_od = serializers.DateField()
    datazak_do = serializers.DateField()
    uwagi = serializers.CharField()
    id_uwagi = serializers.IntegerField()


class SzczPromCentSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    #id_pprom = serializers.IntegerField()
    #id_prom = serializers.CharField()
    #id_prom = models.IntegerField()
    id_tow = serializers.IntegerField()
    bar_kod_tow = serializers.CharField()
    cena_d_tow = serializers.IntegerField()
    nazwa_tow = serializers.CharField()
    cena_d_old = serializers.IntegerField()
    cena_d_prom = serializers.IntegerField()
    #ilosc_prog = serializers.IntegerField()
    cena_zakupu = serializers.IntegerField()


# class PromCentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Nag_rach
#         fields = (
#             'status',
#             'id_nagrach',
#             'numer_rach',
#             'data_operacji',
#             'typ_rach',
#             'od_dnia',
#             'do_dnia',
#             'uwagi',
#             'stat_prom',
#             'id_ref_nagrach',
#             'user_id',
#         )
