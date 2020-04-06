# def <function_name>([<parameters>]):
#     <statement(s)>

def f(qty, item, price):
    print(f'{qty} {item} cost ${price:.2f}')

f('bananas', 1.74, 6)
f(qty=6, item='bananas', price=1.74)
f(6, price=1.74, item='bananas')

def f(qty=6, item='bananas', price=1.74):
    print(f'{qty} {item} cost ${price:.2f}')

f(4)
f()
f(item='kumquats', qty=9)

# Mutable Default Parameter Values
def f(my_list=[]):
    my_list.append('###')
    return my_list

f(['foo', 'bar', 'baz'])
f([1, 2, 3, 4, 5])

def f(my_list=None):
    if my_list is None:
        my_list = []
        my_list.append('###')
    return my_list

def f(*args):
    print(args)
    print(type(args), len(args))
    for x in args:
            print(x)

def avg(*args):
    return sum(args) / len(args)

f(1, 2, 3)
f('foo', 'bar', 'baz', 'qux', 'quux')


# Argument Tuple Unpacking
def f(x, y, z):
    print(f'x = {x} y = {y} z = {z}')

f(1, 2, 3)
t = ('foo', 'bar', 'baz')
f(*t)
a = ['foo', 'bar', 'baz']
f(*a)
s = {1, 2, 3}
f(*s)


def f(*args):
    print(type(args), args)

a = ['foo', 'bar', 'baz', 'qux']
f(*a)

def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]
print(my_sum(*list1, *list2, *list3))


my_list = [1, 2, 3, 4, 5, 6]
a, *b, c = my_list
print(a)
print(b)
print(c)

# Argument Dictionary Packing
def f(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, val in kwargs.items():
            print(key, '->', val)

f(foo=1, bar=2, baz=3)

# Argument Dictionary Unpacking
def f(a, b, c):
    print(F'a = {a} b = {b} c = {c}')

d = {'a': 'foo', 'b': 25, 'c': 'qux'}
f(**d)
f(a='foo', b=25, c='qux')
f(**dict(a='foo', b=25, c='qux'))

def f(a, b, *args, **kwargs):
    print(F'a = {a} b = {b} args = {args} kwargs = {kwargs}', sep='\n')

# Multiple Unpackings
def f(*args):
    for i in args: print(i)

a = [1, 2, 3]
t = (4, 5, 6)
s = {7, 8, 9}
f(*a, *t, *s)

def f(**kwargs):
    for k, v in kwargs.items(): print(k, '->', v)

d1 = {'a': 1, 'b': 2}
d2 = {'x': 3, 'y': 4}
f(**d1, **d2)

# Keyword-Only Arguments
def concat(*args):
    print(f'-> {".".join(args)}')

concat('a', 'b', 'c')

def concat(prefix, *args):
    print(f'{prefix}{".".join(args)}')

concat('//', 'a', 'b', 'c')

def concat(*args, prefix='-> '):
    print(f'{prefix}{".".join(args)}')

concat('a', 'b', 'c', prefix='... ')

def concat(*args, prefix='-> ', sep='.'):
    print(f'{prefix}{sep.join(args)}')

concat('a', 'b', 'c')

# docstring
def avg(*args):
    """Returns the average of a list of numeric values."""
    return sum(args) / len(args)

# Python Function Annotations
def f(a: '<a>', b: '<b>') -> '<ret_value>':
    pass

def f(a: int, b: str) -> float:
    print(a, b)
    return(3.5)

f.__annotations__
f.__annotations__['a']
f.__annotations__['b']
f.__annotations__['return']

def area(
    r: {
           'desc': 'radius of circle',
           'type': float
       }) -> \
       {
           'desc': 'area of circle',
           'type': float
       }:
    return 3.14159 * (r ** 2)
area.__annotations__
area.__annotations__['r']['desc']
area.__annotations__['return']['type']

# Enforcing Type-Checking
def f(a: int, b: str, c: float):
    import inspect
    args = inspect.getfullargspec(f).args
    annotations = inspect.getfullargspec(f).annotations
    for x in args:
        print(x, '->',
              'arg is', type(locals()[x]), ',',
              'annotation is', annotations[x],
              '/', (type(locals()[x])) is annotations[x])