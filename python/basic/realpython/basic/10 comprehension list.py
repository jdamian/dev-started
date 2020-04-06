# list comprehension#
# new_list = [expression for member in iterable]
# new_list = [expression for member in iterable]
# new_list = [expression for member in iterable (if conditional)]
# new_list = [expression (if conditional) for member in iterable]

squares = []
for i in range(10):
    squares.append(i * i)

squares = [i * i for i in range(10)]

txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08
def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)

final_prices = map(get_price_with_tax, txns)
list(final_prices)

final_prices = [get_price_with_tax(i) for i in txns]


sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels
consonants = [i for i in sentence if is_consonant(i)]

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]

quote = "life, uh, finds a way"
unique_vowels = {i for i in quote if i in 'aeiou'}

squares = {i: i * i for i in range(10)}

# Walrus Operator
import random
def get_weather_data():
    return random.randrange(90, 110)
hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
