from django.db import models
from django.contrib.auth.models import AbstractUser, User

# App specific user model
class UserProfile(AbstractUser):
    # The additional attributes we wish to include.
    yammer_url = models.URLField(blank=True)

    def __unicode__(self):
        return self.username


class UserMetrics(models.Model):
    user = models.ForeignKey(UserProfile, unique=True, related_name='user')

    times_won = models.IntegerField(blank=True, default=0)
    times_known = models.IntegerField(blank=True, default=0)

    class Meta:
        ordering = ["user__last_name"]
        verbose_name = "User Metric"
        verbose_name_plural = "User Metrics"

    def __unicode__(self):
        return self.user.get_full_name() + " - lifetime points: " + str(self.times_won)


class MostKnown(models.Model):
    most_known_colleague = models.CharField(max_length=200, blank=True)
    # Timestamp for each entry for historical graphing
    date_time = models.DateField('Timestamp')

    class Meta:
        verbose_name = "Most known Colleague"
        verbose_name_plural = "Most known Colleagues"


class GlobalMetrics(models.Model):
    network = models.CharField(max_length=200, blank=True, unique=True)
    most_known = models.ForeignKey(MostKnown)

    class Meta:
        verbose_name = "Global Metric"
        verbose_name_plural = "Global Metrics"

class Suggestions(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    suggestion = models.TextField(max_length=500)

    def __unicode__(self):
        return self.suggestion

    class Meta:
        verbose_name = "Suggestion"
        verbose_name_plural = "Suggestions"
