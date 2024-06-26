import functools
import logging


def log(filename=None):
    """Декоратор принимает аргумент который определяет путь к файлу, в который будут записываться логи"""
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO)

    def decorator(func):
        """Непосредственно обертка функции"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    logging.info(f"{func.__name__} ok")
                    print(result)
                else:
                    print(f"{func.__name__} ok")
                    print(result)
                return result
            except Exception as e:
                if filename:
                    logging.error(f"{func.__name__} error: {e} Inputs {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e} Inputs {args}, {kwargs}")
                raise
        return wrapper
    return decorator
