from functools import wraps

def coroutine(func):
    """Decorator that primes 'func' by advancing to its first yield"""
    @wraps(func)
    def primer(*args, **kwargs):
        generator = func(*args, **kwargs)
        next(generator)
        return generator
    return primer