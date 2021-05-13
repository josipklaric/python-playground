def greet(name):
    return 'Hello ' + name

# Test function
def _test():
    assert(greet('Josip')) == 'Hello Josip'

if __name__ == '__main__':
    _test()