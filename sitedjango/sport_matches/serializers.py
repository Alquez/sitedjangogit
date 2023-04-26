from rest_framework import serializers
from sport_matches.models import SportType, Match


class SportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportType
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    sport_type = SportTypeSerializer()

    class Meta:
        model = Match
        fields = '__all__'