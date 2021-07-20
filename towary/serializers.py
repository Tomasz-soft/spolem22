from django.db.models.base import Model
from rest_framework import serializers
from towary.models import Towary

class TowarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Towary
        fields=(
            'status' ,
            'id_tow' ,
            'id_gtow',
            'id_dtow',
            'id_branz' ,
            'atribs_tow' ,
            'naz_kas_tow' ,
            'nazwa_tow' ,
            'ident_tow' ,
            'bar_kod_tow' ,
            'gr_rabat_t' 
        )