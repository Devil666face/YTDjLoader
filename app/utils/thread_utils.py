from concurrent.futures import ThreadPoolExecutor
from functools import wraps

_DEFAULT_POOL = ThreadPoolExecutor()


def threadpool(f, executor=None):
    @wraps(f)
    def wrap(*args, **kwargs):
        return (executor or _DEFAULT_POOL).submit(f, *args, **kwargs)

    return wrap
