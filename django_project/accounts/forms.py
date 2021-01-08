""" forms for accounts """

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    """ class for user creation
        get_user_model
        uses AUTH_USER_MODEL = 'accounts.CustomUser'
        from config/settings
        to get the user model
    """

    class Meta:
        """ model, fields to use from model """
        model = get_user_model()
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):
    """ class for user change
        get_user_model
        uses AUTH_USER_MODEL = 'accounts.CustomUser'
        from config/settings
        to get the user model
    """

    class Meta:
        """ model, fields to use from model """
        model = get_user_model()
        fields = ('email', 'username',)
