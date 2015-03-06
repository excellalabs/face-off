from core.models import Metrics

def post_user_creation(backend, user, response, *args, **kwargs):
    if backend.name == 'yammer' and not user.yammer_url:
        user.yammer_url = response['user']['mugshot_url_template']
        user.save()
        Metrics.objects.create(user=user).save()