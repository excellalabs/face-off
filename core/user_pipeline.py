from core.models import UserMetrics

def post_user_creation(backend, user, response, *args, **kwargs):
    if backend.name == 'yammer' and not user.yammer_url:
        user.yammer_url = response['user']['mugshot_url_template']
        user.upload_image_url = response['user']['web_url']
        user.save()
        UserMetrics.objects.create(user=user).save()