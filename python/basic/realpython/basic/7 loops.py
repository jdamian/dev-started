# while
# while <expr>:
#     <statement(s)>
# else:
#     <additional_statement(s)>     # executed only if the loop terminates “by exhaustion”, If the loop is exited by a break statement, the else clause won’t be executed.

n = 5
while n > 0:
    n -= 1
    print(n)

while n > 0: n -= 1; print(n)

a = ['foo', 'bar', 'baz']
while a:
    print(a.pop(-1))

a = ['foo', 'bar', 'baz', 'qux']
s = 'corge'
i = 0
while i < len(a):
    if a[i] == s:
        # Processing for item found
        break
    i += 1
else:
    # Processing for item not found
    print(s, 'not found in list.')


# for

# Collection-Based or Iterator-Based Loop
# for i in <collection>
#     <loop body>
# for <var> in <iterable>:
#     <statement(s)>

a = ['foo', 'bar', 'baz']
for i in a:
    print(i)

d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)    # key
    print(d[k]) # values

for v in d.values():
    print(v)    #value

for k,v in d.items():
    print(k)    # key
    print(v)    # value

x = range(5)    # object range
x = range(5, 20, 3)
x = range(-5, 5)
x = range(5, -5, -1)

for n in x:
    print(n)

for i in a:
    print(i)
else:
    print('Done.')  # Will execute

for i in reversed(range(5)):
    print(i)

import numpy as np
np.arange(0.3, 1.6, 0.3)

for i in np.arange(0.3, 1.6, 0.3):
    print(i)


