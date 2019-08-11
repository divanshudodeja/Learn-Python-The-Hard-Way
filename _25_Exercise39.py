states = {
   'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

cities = {
    'CA' : 'San Fransisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])

print('-' * 10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" %(state, abbrev))

print('-' * 10)
state = states.get('Texas', None)

if not state:
    print("Sorry, no Texas")