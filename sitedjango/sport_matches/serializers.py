from rest_framework import serializers
from sport_matches.models import SportType, Match, Team


class TeamSerializator(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('name', 'logo')
class SportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportType
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    sport_type = SportTypeSerializer()
    team_one = TeamSerializator()
    team_two = TeamSerializator()
    date = serializers.DateField(format='%Y.%m.%d')
    time = serializers.TimeField(format='%H:%M')

    class Meta:
        model = Match
        fields = '__all__'