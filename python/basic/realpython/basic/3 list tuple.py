# list
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
b = ['baz', 'qux', 'bar', 'foo']

a == b
a is b
a[-1]
a[2:5]
a[-5:-2]
a[0:6:2]
a[::-1]
a[:]
a[:] is a
'qux' in a
'thud' not in a
a + ['grault', 'garply']
a * 2
len(a)
min(a)
max(a)

# a[m:n] = <iterable>
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
a[1:6] = ['Bark!']
a[1:2] = [2.1, 2.2, 2.3]
a[1] = [2.1, 2.2, 2.3]
a[2:2] = [3, 4, 5, 6]
a[1:5] = []
del a[1:5]
del a[3]

a += ['grault', 'garply']
a = [10, 20] + a
a += 'corge'
a += ['corge']

a.append(123)
a + [1, 2, 3]
a.append([1, 2, 3])
a.append('foo')
a.extend([1, 2, 3])
a.insert(3, 3.14159)
a.remove('baz')
a.pop()
a.pop(1)
a.pop(-3)

a[2:2] = [1, 2, 3]
a += [3.14159]
a[2:3] = []
del a[0]

# tuples
t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
t[0]
t[-1]
t[1::2]
t[::-1]
t = (2,)


t = 1, 2, 3
t = 2,

# Tuple Unpacking
t = ('foo', 'bar', 'baz', 'qux')
(s1,s2,s3,s4) = t

t = 1, 2, 3
x1, x2, x3 = t
x1, x2, x3 = 4, 5, 6

a, b = b, a # swap variable