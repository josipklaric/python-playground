from caster.caster import as_int

def add(x, y):
    return as_int(x) + as_int(y)

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def devide(x, y):
    return x / y

# Test function
def _test():
    assert add(1,2) == 3
    assert add('1','2') == 3

if __name__ == '__main__':
    _test()
