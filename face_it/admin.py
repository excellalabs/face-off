from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from core.models import UserMetrics, UserProfile, GlobalMetrics, MostKnown, Suggestions, ColleagueGraph


class ColleagueGraphResource(resources.ModelResource):
    class Meta:
        model = ColleagueGraph


class UserMetricsResource(resources.ModelResource):

    class Meta:
        model = UserMetrics


class GlobalMetricsResource(resources.ModelResource):
    class Meta:
        model = GlobalMetrics


class MostKnownResource(resources.ModelResource):
    class Meta:
        model = MostKnown

class SuggestionsResource(resources.ModelResource):
    class Meta:
        model = Suggestions

class ColleagueGraphAdmin(ImportExportActionModelAdmin):
    resource_class = ColleagueGraphResource

class UserMetricsAdmin(ImportExportActionModelAdmin):
    resource_class = UserMetricsResource


class GlobalMetricsAdmin(ImportExportActionModelAdmin):
    resource_class = GlobalMetrics


class MostKnownAdmin(ImportExportActionModelAdmin):
    resource_class = MostKnown

class SuggestionsAdmin(ImportExportActionModelAdmin):
    resource_class = SuggestionsResource

class UserProfileAdmin(admin.ModelAdmin):
    fields = []


admin.site.register(UserProfile),
admin.site.register(GlobalMetrics, GlobalMetricsAdmin)
admin.site.register(MostKnown, MostKnownAdmin)
admin.site.register(UserMetrics, UserMetricsAdmin)
admin.site.register(Suggestions, SuggestionsAdmin)
admin.site.register(ColleagueGraph, ColleagueGraphAdmin)