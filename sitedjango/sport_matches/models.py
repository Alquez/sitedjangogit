from django.db import models

class SportType(models.Model):
    name = models.CharField(max_length=100)
    logo = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    logo = models.URLField(blank=True)
    # sport_type = models.ForeignKey(SportType, on_delete=models.CASCADE, related_name='sport_type')
    def __str__(self):
        return self.name


class Match(models.Model):
    name = models.CharField(blank=True)
    url = models.URLField(blank=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    team_one = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_one',blank=False)
    team_two = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_two',blank=False)
    sport_type = models.ForeignKey(SportType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.team_one} vs {self.team_two}"