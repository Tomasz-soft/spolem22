from rest_framework import serializers
from prominfo.models import PromCentInfo, PromCentInfoOnly


class PromCentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromCentInfo
        fields = (
            'datazak_od',
            'datazak_do',
            'uwagi',
            'id_prac',
            'nr_prom',
            'nazwa_prom',
        )


class PromCentInfoOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = PromCentInfoOnly
        fields = (
            'datazak_od',
            'datazak_do',
            'uwagi',
            'id_prac',
            'nr_prom',
            'nazwa_prom',
        )


class PromCentInfoOnlySerializer2(serializers.Serializer):
    datazak_od = serializers.DateField()
    datazak_do = serializers.DateField()
    uwagi = serializers.CharField()
    id_prac = serializers.IntegerField()
    nazwa_prom = serializers.CharField()
    data_b_prom = serializers.DateField()
    data_e_prom = serializers.DateField()
    numer_rach = serializers.CharField()
