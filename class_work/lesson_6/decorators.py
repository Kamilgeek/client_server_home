import logging
import inspect
from functools import wraps
from datetime import datetime

logger = logging.getLogger('decorators')
# def sample(text, num):
#     return text * num
#
# def logged(func):
#     def wrapper(text, num):
#         result = func(text, num)
#         print(f'log - {func.__name__}({text, num}) = {result} ')
#         return result
#     return wrapper
#
# sample_clone = logged(sample)
# sample_clone('text', 3)
#
# @logged
# def sample(text, num):
#      return text * num

# # sample('text', 3)
#
# def delimited(func):
#     def wrapper(*args, **kwargs):
#         print('*' * 50)
#         return func(*args, **kwargs)
#     return wrapper
#
# # @logged
# # @delimited
# # def sample(text, num):
# #      return text * num
#
# # sample('text', 3)
#
# # def logged(log_format):
# #     def decorator(func):
# #         def wrapper(text, num):
# #             result = func(text, num)
# #             name = func.__name__
# #             args = ','.join((text, str(num)))
# #             print(log_format % {'name': name, 'args': args, 'result': result})
# #             return result
# #         return wrapper
# #     return decorator
# #
# #
# # def sample(text, num):
# #     return text * num
# #
# # decorator = logged('%(name)s(%(args)s) = %(result)s')
# # sample_clone = decorator(sample)
# # sample_clone('sample', 2)
#
# # def logged(log_format):
# #     def decorator(func):
# #         def wrapper(text, num):
# #             result = func(text, num)
# #             name = func.__name__
# #             args = ','.join((text, str(num)))
# #             print(log_format % {'name': name, 'args': args, 'result': result})
# #             return result
# #         return wrapper
# #     return decorator
#
# def logged(log_format):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(text, num):
#             result = func(text, num)
#             name = func.__name__
#             args = ','.join((text, str(num)))
#             print(log_format % {'name': name, 'args': args, 'result': result})
#             return result
#         return wrapper
#     return decorator
#
#
#
# @logged('%(name)s(%(args)s) = %(result)s')
# def sample(text, num):
#     return text * num
#
# sample('sample', 4)
# print(sample.__name__)

def log(func):
    @wraps(func)
    def wrapper( *args, **kwargs):
        print(f'{datetime.now()}, была вызвана функция {func.__name__} из функции {inspect.stack()[1][3]}')
        # logger.debug(f'{datetime.now()}, была вызвана функция {func.__name__} из функции {inspect.stack()}')
        return func( *args, **kwargs)
    return wrapper
@log
def func_z():
    pass

def second():
    func_z()

second()

