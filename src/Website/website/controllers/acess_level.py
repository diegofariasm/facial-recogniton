from functools import wraps
from flask import redirect, url_for, session
def requires_access_level(user, access_level):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not user.is_allowed(access_level):
                return redirect(url_for('routes.home', message="Voce não tem acesso a essa página."))
            return f(*args, **kwargs)
        return decorated_function
    return decorator