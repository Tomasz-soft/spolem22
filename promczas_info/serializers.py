from rest_framework import serializers
from promczas_info.models import PromCzasInfoOnly, PromCzasInfo


class PromCzasInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromCzasInfo
        fields = (
            'datazak_od',
            'datazak_do',
            'uwagi',
            'id_prac',
            'nr_prom',
        )


class PromCzasInfoOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = PromCzasInfoOnly
        fields = (
            'datazak_od',
            'datazak_do',
            'uwagi',
            'id_prac',
            'nr_prom',
        )
