from core.models import UserProfile


class UserProfileAuthBackend(object):
    def authenticate(self, username=None, password=None):
        if username and password:
            try:
                user = UserProfile.objects.get(username=username)
                if user.check_password(password):
                    return user
            except UserProfile.DoesNotExist:
                pass
        return None


    def get_user(self, user_id):
        try:
            return UserProfile.objects.get(pk=user_id)
        except UserProfile.DoesNotExist:
            return None
