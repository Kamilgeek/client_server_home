def sample(text, num):
    return text * num

def logged(func):
    def wrapper(text, num):
        result = func(text, num)
        print(f'log - {func.__name__}({text, num}) = {result} ')
        return result
    return wrapper

sample_clone = logged(sample)
sample_clone('text', 3)

