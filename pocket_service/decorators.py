from django.shortcuts import redirect

def login_required(view_func):
    """
    Decorator to check if the user is logged in.
    If not logged in, redirect to the login page.
    """

    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            # User is not logged in, redirect to the login page
            return redirect('login_page')  # Adjust 'login' to your actual login URL
        return view_func(request, *args, **kwargs)

    return wrapper


def admin_required(view_func):
    """
    Decorator to check if the user is an admin.
    If not an admin, redirect to a designated page.
    """

    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            # User is not an admin, redirect to a designated page
            return redirect('login')  # Adjust 'not_admin' to your designated page URL
        return view_func(request, *args, **kwargs)

    return wrapper
