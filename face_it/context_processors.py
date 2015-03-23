def global_suggestion_form(request):
    from core.forms import SuggestionForm
    return {'global_suggestion_form': SuggestionForm()}
