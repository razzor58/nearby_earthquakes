from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print("\nExecution time: {:.2f} sec.".format(te - ts))
        return result

    return wrap
