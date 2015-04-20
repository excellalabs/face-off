def global_suggestion_form(request):
    from core.forms import SuggestionForm
    return {'global_suggestion_form': SuggestionForm()}

def yammer_client_id(request):
    from django.conf import settings
    return {'app_id': settings.SOCIAL_AUTH_YAMMER_KEY}

