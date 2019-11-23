import logging
import inspect
from datetime import datetime
from functools import wraps
from protocol import make_response

logger = logging.getLogger('decorators')

def logged(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        logger.debug(f'{func.__name__}: {request}')
        return func(request,  *args, **kwargs )
    return wrapper

def login_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if 'token' not in request :
            return make_response(request, 403, 'Access denied')
        return func(request, *args, **kwargs)
    return wrapper

def log(func):
    @wraps(func)
    def wrapper( *args, **kwargs):
        print(f'{datetime.now()}, была вызвана функция {func.__name__} из функции {inspect.stack()[1][3]}')
        # logger.debug(f'{datetime.now()}, была вызвана функция {func.__name__} из функции {inspect.stack()}')
        return func( *args, **kwargs)
    return wrapper