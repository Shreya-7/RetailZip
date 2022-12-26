
from flask import render_template, redirect, request

import traceback


def misc_error(my_function):
    """
        Miscellaneous Error Decorator
    """
    def wrap(*args, **kwargs):
        try:
            return my_function(*args, **kwargs)
        except:
            print(traceback.print_exc())
            return render_template('error.html')

    wrap.__name__ = my_function.__name__
    return wrap


def redirect_to_https(my_function):
    """
        Redirects incoming HTTP calls to HTTPS
    """
    def wrap(*args, **kwargs):
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            print('Redirecting...')
            return redirect(url, code=code)
        
        return my_function(*args, **kwargs)

    wrap.__name__ = my_function.__name__
    return wrap