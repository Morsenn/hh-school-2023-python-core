import time

from functools import wraps


def invocation_logger(logger):
    """
    logger - функция, принимающая на вход один аргумент - имя функции,
    вызовы которой логгируются
    """
    def function_decorator(func):
        @wraps(func)
        def function_wrapper(*args, **kwargs):
            logger(func.__name__)
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f'Время выполнения {func.__name__}: {end_time - start_time} секунд')
            return result
        return function_wrapper
    return function_decorator
