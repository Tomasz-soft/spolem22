from rest_framework import serializers
from sklepy.models import Sklepy


class SklepySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sklepy
        fields = (
            'db_id',
            'db_name',
            'db_ident',
            'archive'
        )
