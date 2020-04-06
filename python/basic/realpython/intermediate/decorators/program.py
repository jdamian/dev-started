from decorators import do_twice
from decorators import timer
from decorators import debug
from decorators import slow_down
from decorators import register
import math

@do_twice
def say_whee():
    print('Whee!')

@do_twice
def greet(name):
    print(f"Hello {name}")

@do_twice
def return_greeting(name):
    print('Creating greeting')
    return f'Hi {name}'

print('begin')
say_whee()
greet('juan')
print(return_greeting('test'))




# @my_decorator
# def say_whee():
#     print("Whee!")

# say_whee()



# @not_during_the_night
# def say_whee1():
#     print("Whee!")

# say_whee1()

# def greet_bob(greeter_func):
#     return greeter_func('Bob')


# def say_hello(name):
#     return f'Hello {name}'

# def be_awesome(name):
#     return f'Yo {name}, together we are the awesomest!'


# saludo = greet_bob(say_hello)
# print(saludo)

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(1000)

@debug
def make_greeting(name,age=None):
    if age is None:
        return f'Howdy {name}!'
    else:
        return f'Whoa {name}! {age} already, you are growing up!'

print(make_greeting("Benjamin"))
print(make_greeting("Richard", age=112))
print(make_greeting(name="Dorrisile", age=116))


# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

print(approximate_e(5))

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

countdown(3)



