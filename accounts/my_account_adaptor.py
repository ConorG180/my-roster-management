"""Account adapter to restrict users access to
signup/registration form if they don't have
the "is_staff" property set to True."""
from allauth.account.adapter import DefaultAccountAdapter


class NoNewUsersAccountAdapter(DefaultAccountAdapter):
    """Adapter to disable allauth new signups if user
    doesn't have authorisation. Used at
    equilang/settings.py with key ACCOUNT_ADAPTER
    https://django-allauth.readthedocs.io/en/latest/advanced.html#custom-redirects """

    def is_open_for_signup(self, request):
        """Checks whether or not the site is open for
        signups based on the users is_staff status.
        This prevents unathorised users from registering
        new accounts in the programme by brute-forcing the
        accounts/signup url. """

        user = request.user
        if user.is_staff:
            return True
        else:
            return False
