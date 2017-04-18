y = 7


def foo():
    return y


def add5(x):
    return x + 5


def get_remainder(x):
    return x % 2


def get_gender(chromosome1, chromosome2):
    if chromosome1 + chromosome2 == 'xx':
        return 'female'
    elif chromosome1 + chromosome2 == 'xy':
        return 'male'
    elif chromosome1 + chromosome2 == 'yx':
        return 'male'
    else:
        return 'invalid'

