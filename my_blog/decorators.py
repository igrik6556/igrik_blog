from django.http import Http404


def superuser_check(func):
    """
    Decorator for views that checks that the user is superuser.
    If not, the error 404 is raised.
    """
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser:
            return func(request, *args, **kwargs)
        raise Http404
    return wrapper
