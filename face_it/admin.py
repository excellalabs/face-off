from django.contrib import admin
from core.models import UserMetrics, UserProfile, GlobalMetrics, MostKnown


admin.site.register(UserMetrics)
admin.site.register(UserProfile)
admin.site.register(GlobalMetrics)
admin.site.register(MostKnown)