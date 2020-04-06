MLB_team = {
    'Colorado' : 'Rockies',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle'  : 'Mariners'
}

MLB_team = dict([
    ('Colorado', 'Rockies'),
    ('Boston', 'Red Sox'),
    ('Minnesota', 'Twins'),
    ('Milwaukee', 'Brewers'),
    ('Seattle', 'Mariners')
])

MLB_team = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Mariners'
)

type(MLB_team)
print(MLB_team)
print(MLB_team['Minnesota'])
MLB_team['Kansas City'] = 'Royals'  # adding
MLB_team['Seattle'] = 'Seahawks'    # update

person = {}
type(person)
person['fname'] = 'Joe'
person['lname'] = 'Fonebone'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
person['children']
person['children'][-1]
person['pets']['cat']

'Milwaukee' in MLB_team
'Toronto' not in MLB_team
'Toronto' in MLB_team and MLB_team['Toronto']
len(MLB_team)

d = {'a': 10, 'b': 20, 'c': 30}
d.clear()
print(d.get('b'))
list(d.items())
list(d.keys())
list(d.values())
d.pop('b')
d.pop('z', -1)
d.popitem()

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
d1.update(d2)
d1.update([('b', 200), ('d', 400)])
d1.update(b=200, d=400)


