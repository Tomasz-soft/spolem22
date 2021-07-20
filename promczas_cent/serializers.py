from rest_framework import serializers
from promczas_cent.models import PromocjaCzas, PromocjaCzas_pozycja

class PromocjaCzasSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    id_pczas = serializers.IntegerField()
    godz_prom = serializers.IntegerField()
    dt_prom = serializers.IntegerField()
    mr_prom = serializers.IntegerField()
    data_p_od = serializers.DateField()
    data_p_do = serializers.DateField()
    nr_prom = serializers.IntegerField()
    nazwa_prom = serializers.CharField()
    nr_rabat_k = serializers.IntegerField()
    typ_prom = serializers.IntegerField()
    uwagi_prom = serializers.CharField()
    data_mod = serializers.DateTimeField()
    user_id = serializers.IntegerField()
    kwota_prog = serializers.IntegerField()
    max_prom = serializers.IntegerField()
    datazak_od = serializers.DateField()
    datazak_do = serializers.DateField()
    uwagi = serializers.CharField()


# class PromocjaCzasSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PromocjaCzas
#         fields = (
#             'status',
#             'id_pczas',
#             'godz_prom',
#             'dt_prom',
#             'mr_prom',
#             'data_p_od',
#             'data_p_do',
#             'nr_prom',
#             'nazwa_prom',
#             'nr_rabat_k',
#             'typ_prom',
#             'uwagi_prom',
#             'data_mod',
#             'user_id',
#             'kwota_prog',
#             'max_prom',
#             'datazak_od',
#             'datazak_do',
#             'uwagi'
#         )


# class PromocjaCzasPozycjeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PromocjaCzas_pozycja
#         fields = (
#             'id_pczasp',
#             'status',
#             'id_prom_czas',
#             'id_tow',
#             'rabat',
#             'nr_poz',
#             'attr_prom',
#             'ilosc_prom',
#             'kwota_rab',
#             'cena_d_prom',
#             'ilosc_plat',
#             'ilosc_pkt',
#             'przelicz'
#         )

class PromocjaCzasPozycjaSerializer(serializers.Serializer):

    id_pczasp = serializers.IntegerField()
    status = serializers.IntegerField()
    id_prom_czas = serializers.IntegerField()
    id_tow = serializers.IntegerField()
    nazwa_tow = serializers.CharField()
    bar_kod_tow = serializers.CharField()
    rabat = serializers.IntegerField()
    nr_poz = serializers.IntegerField()
    attr_prom = serializers.IntegerField()
    ilosc_prom = serializers.IntegerField()
    kwota_rab = serializers.IntegerField()
    cena_d_prom = serializers.IntegerField()
    ilosc_plat = serializers.IntegerField()
    ilosc_pkt = serializers.IntegerField()
    przelicz = serializers.IntegerField()
    nazwa_prom = serializers.CharField()
    nr_prom = serializers.IntegerField()
    typ_prom = serializers.IntegerField()
