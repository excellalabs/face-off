from django.db import models
from django.contrib.auth.models import AbstractUser, User

# App specific user model
class UserProfile(AbstractUser):
    # The additional attributes we wish to include.
    yammer_url = models.URLField(blank=True)

    def __unicode__(self):
        return self.username


class Metrics(models.Model):
    user = models.ForeignKey(UserProfile, unique=True, related_name='user')

    times_won = models.IntegerField(blank=True, default=0)
    times_known = models.IntegerField(blank=True, default=0)

    class Meta:
        ordering = ["user__last_name"]

    def __unicode__(self):
        return self.user.full_name