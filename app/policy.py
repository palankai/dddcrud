class Specification:

    def is_satisfied(self, cmd):
        return False

class PhoneNumberLongEnough(Specification):

    def is_satisfied(self, cmd):
        return len(cmd.phone) > 3

    def __str__(self):
        return self.__class__.__name__


def policy(*policies):
    def decorator(func):
        func.policies = policies
        return func
    return decorator
