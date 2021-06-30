from django.contrib.auth import authenticate

from Full_Stack.settings import SOCIAL_SECRET
from user.models import CustomUser
import random
from rest_framework.exceptions import AuthenticationFailed



def generate_username(name):

    username = "".join(name.split(' ')).lower()
    if not CustomUser.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)


def register_social_user(provider, email, name):
    filtered_user_by_email = CustomUser.objects.filter(email=email)

    if filtered_user_by_email.exists():

        if provider == filtered_user_by_email[0].auth_provider:

            registered_user = authenticate(
                username=email, password=SOCIAL_SECRET)
            return {
                'username': registered_user.username,
                'email': registered_user.email,
                'tokens': registered_user.tokens()}

        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

    else:
        user = {
            'username': generate_username(name), 'email': email,
            'password': SOCIAL_SECRET}

        user = CustomUser.objects.create_user(**user)
        user.is_active = True
        user.activation_code = ''
        user.auth_provider = provider
        user.save()
        return 'Successfully registered'