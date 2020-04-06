# if <expr>:
#     <statement(s)>
# elif <expr>:
#     <statement(s)>
# elif <expr>:
#     <statement(s)>
#     ...
# else:
#     <statement(s)>

x = 0
y = 5

if x < y:
    print('yes')

if x:
    pass
if x or y :
    pass
if x and y:
    pass
if 'au' in ' grault':
    pass

if 'quux' in ['foo', 'bar', 'baz']:
    pass

names = {
    'Fred': 'Hello Fred',
    'Xander': 'Hello Xander',
    'Joe': 'Hello Joe',
    'Arnold': 'Hello Arnold'
}
print(names.get('Joe', "I don't know who you are!"))
print(names.get('Rick', "I don't know who you are!"))

if 'f' in 'foo': print('1'); print('2'); print('3')

x = 2
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')

# Ternary Operator)
# <expr1> if <conditional_expr> else <expr2>
raining = False
print("Let's go to the", 'beach' if not raining else 'library')
raining = True
print("Let's go to the", 'beach' if not raining else 'library')
age = 12
s = 'minor' if age < 21 else 'adult'
'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'

a=1
b=2
m = a if a > b else b

x = y = 40
z = 1 + x if x > y else y + 2
z = (1 + x) if x > y else (y + 2)
z = 1 + (x if x > y else y) + 2

'foo' if True else 1/0
1/0 if False else 'bar'
