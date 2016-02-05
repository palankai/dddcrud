import functools


class Specification:

    def is_satisfied(self, cmd):
        return False

class PhoneNumberLongEnough(Specification):

    def is_satisfied(self, cmd):
        return len(cmd.phone) > 3


def policies(*args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, cmd):
            for p in args:
                if not p.is_satisfied(cmd):
                    print('ERROR: %s' % p.__class__.__name__)
                    return
            return func(self, cmd)
        return wrapper
    return decorator
