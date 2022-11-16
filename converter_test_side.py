print()
print("Welcome to Brandon and Logan's Unit Converter Program")
print("for conversions with LQ those will spesify LQ conversions")
print()


conversions_available = [(1, '°F', '°C'),
                         (2, '°C', '°F'),
                         (3, 'kg', 'lbs'),
                         (4, 'lbs', 'kg'),
                         (5, 'Cups', 'fl-oz'),
                         (6, 'fl-oz',  'cups'),
                         (7, 'Cups', 'Tbs'),
                         (8, 'Tbs',  'Cups'),
                         (9, 'Cups',  'Pint'),
                         (10, 'Pint', 'Cups'),
                         (11, 'Cups', 'Teaspoons' ),
                         (12, 'Teaspoons', 'Cups'),
                         (13, 'Cups', 'Quarts'),
                         (14, 'Quarts', 'Cups'),
                         (15, 'Cups', 'Gallons'),
                         (16, 'Gallons', 'Cups'),
]

print("Available Conversions")
print()

for conversion_number, from_unit, to_unit in conversions_available:
    print(f'{conversion_number}) {from_unit} -> {to_unit}')

print()
conversion = input('Enter the number of the conversion to use --> ')
conversion_index =int(conversion) - 1

conversion_number, from_unit, to_unit = conversions_available[conversion_index]
print()
from_value = float(input(f'Enter {from_unit} --> ' ))
print()

if conversion_number == 1:
    to_value = (from_value - 32) / 1.8
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}') 

elif conversion_number == 2:
    to_value = from_value * 1.8 + 32
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 3:
    to_value = from_value * 0.45
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 4:
    to_value = from_value * 2.22
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 5:
    to_value = from_value * 8
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}') 

elif conversion_number == 6:
    to_value = from_value / 8
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 7:
    to_value = (from_value *16)
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 8:
    to_value = (from_value /16)
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 9:
    to_value = (from_value /2)
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 10:
    to_value = (from_value *2)
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')    

elif conversion_number == 11:
    to_value = from_value * 48
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 12:
    to_value = from_value / 48
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 13:
    to_value = from_value / 4
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 14:
    to_value = from_value * 4
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 15:
    to_value = from_value / 16
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 16:
    to_value = from_value * 16
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')