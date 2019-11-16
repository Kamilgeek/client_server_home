# def sample(text, num):
#     return text * num
#
def logged(func):
    def wrapper(text, num):
        result = func(text, num)
        print(f'log - {func.__name__}({text, num}) = {result} ')
        return result
    return wrapper
#
# sample_clone = logged(sample)
# sample_clone('text', 3)
#
# @logged
# def sample(text, num):
#      return text * num

# sample('text', 3)

def delimited(func):
    def wrapper(*args, **kwargs):
        print('*' * 50)
        return func(*args, **kwargs)
    return wrapper

@logged
@delimited
def sample(text, num):
     return text * num

sample('text', 3)