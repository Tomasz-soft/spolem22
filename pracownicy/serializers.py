from rest_framework import serializers
from pracownicy.models import Pracownicy


class PracownicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pracownicy
        fields = (
            'status',
            'id_prac',
            'nazw_prac',
            'imie_prac',
            'ident_prac',
            'haslo_prac',
            'klucz_prac',
            'user_id',
        )


class PracLoginSerializer(serializers.Serializer):
    nazw_prac = serializers.CharField()
    imie_prac = serializers.CharField()
    ident_prac = serializers.CharField()
    klucz_prac = serializers.CharField()
    attr_prac = serializers.CharField()
    id_prac = serializers.IntegerField()
    db_id = serializers.IntegerField()
    status = serializers.IntegerField()
    plstatus = serializers.IntegerField()
    #db_name = serializers.CharField()
