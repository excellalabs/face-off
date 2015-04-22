from core.models import UserMetrics, UserProfile
from django.core.exceptions import ObjectDoesNotExist


def post_user_creation(backend, user, response, *args, **kwargs):
    if backend.name == 'yammer' and not user.yammer_url:
        user.yammer_url = response['user']['mugshot_url_template']
        user.upload_image_url = response['user']['web_url']
        user.network = response['user']['network_name']
        user.save()
        UserMetrics.objects.create(user=user).save()
    else:
        user = UserProfile.objects.get(email=response['user']['email'])
        if user.yammer_url != response['user']['mugshot_url_template']:
            user.yammer_url = response['user']['mugshot_url_template']
            user.save()

