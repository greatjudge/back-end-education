import functools
from django.shortcuts import redirect, reverse


def own_login_required(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        request = args[1]
        if request.user.is_authenticated:
            return func(*args, **kwargs)
        return redirect('login')
    return wrapped
