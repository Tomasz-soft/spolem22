from rest_framework import serializers
from promocje.models import Promocje, PozProm


class PromocjeSerializer2(serializers.Serializer):
    status = serializers.IntegerField()
    id_prom = serializers.IntegerField()
    data_d_prom = serializers.DateTimeField()
    data_b_prom = serializers.DateTimeField()
    data_e_prom = serializers.DateTimeField()
    uwagi_prom = serializers.CharField()
    nr_prom = serializers.IntegerField()
    stat_prom = serializers.IntegerField()
    status_prominfo = serializers.IntegerField()
    datazak_od = serializers.DateField()
    datazak_do = serializers.DateField()
    uwagi = serializers.CharField()
    id_prac = serializers.IntegerField()


class PromocjeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocje
        fields = (
            'status',
            'id_prom',
            'data_d_prom',
            'data_b_prom',
            'data_e_prom',
            'uwagi_prom',
            'nr_prom',
            'stat_prom'
        )


class PozPromSerializer(serializers.ModelSerializer):
    class Meta:
        model = PozProm
        fields = (
            'status',
            'id_pprom',
            'id_prom',
            'id_tow',
            'nazwa',
            'cena_d_old',
            'cena_d_prom',
            'ilosc_prom',
            'obrot_prom',
            'id_knt',
            'data_b_prom',
            'data_e_prom',
            'stat_prom',
            'cena_zakupu',
            'ilosc_prog'
        )


class SzczPromSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    #id_pprom = serializers.IntegerField()
    #id_prom = serializers.CharField()
    #id_prom = serializers.IntegerField()
    id_tow = serializers.IntegerField()
    bar_kod_tow = serializers.CharField()
    cena_d_tow = serializers.IntegerField()
    nazwa_tow = serializers.CharField()
    #nazwa_tow = serializers.CharField()
    cena_d_old = serializers.IntegerField()
    cena_d_prom = serializers.IntegerField()
    ilosc_prom = serializers.IntegerField()
    obrot_prom = serializers.IntegerField()
    id_knt = serializers.IntegerField()
    #data_b_prom = serializers.DateTimeField()
    #data_e_prom = serializers.DateTimeField()
    stat_prom = serializers.IntegerField()
    #ilosc_prog = serializers.IntegerField()
