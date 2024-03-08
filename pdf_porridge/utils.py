import time
from loguru import logger
from colorama import Fore, Back, Style, init

init(autoreset=True)


# = Decorators =================================================================


def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        func_name = func.__name__
        logger.info(f"Function '{func_name}' ⚡️{elapsed_time:.6f} sec")
        return result

    return wrapper


# end of file
