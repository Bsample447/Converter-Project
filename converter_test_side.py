print()
print("Welcome to Brandon and Logan's Unit Converter Program")
print()


conversions_available = [(1, '°F', '°C'),
                         (2, '°C', '°F'),
                         (3, 'kg', 'lbs'),
                         (4, 'lbs', 'kg'),
                         (5, 'Cups', 'Fl-Ounces'),
                         (6, 'Fl-Ounces',  'cups'),
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
                         (17, 'Tablespoons', 'Teaspoons'),
                         (18, 'Teaspoons', 'Tablespoons'),
                         (19, 'Tablespoons', 'FlOunces'),
                         (20, 'FlOunces', 'Tablespoons'),
                         (21, 'Tablespoons', 'Cups'),
                         (22, 'Cups', 'Tablespoons'),
                         (23, 'Milliliters', 'Tablespoons'),
                         (24, 'Tablespoons', 'Milliliters'),
                         (25, 'Milliliters', 'Fl-Ounces'),
                         (26, 'Fl-Ounces', 'Milliliters'),
                         (27, 'Cups', 'Millilters'),
                         (28, 'Milliliters', 'Cups'),
                         (29, 'Liters', 'Cups'),
                         (30, 'Cups', 'Liters'),
                         (31, 'Liters', 'Pints'),
                         (32, 'Pints', 'Liters'),
                         (33, 'Liters', 'Quarts'),
                         (34, 'Quarts', 'Liters'),
                         (35, 'Liters', 'Gallons'),
                         (36, 'Gallons', 'Liters'),
                         (37, 'Grams','Ounces'),
                         (38, 'Grams', 'Ounces'),
                         (39, 'Grams', 'Pounds'),
                         (40, 'Pounds', 'Grams'),
                         (41, 'Pounds', 'Ounces'),
                         (42, 'Ounces', 'Pounds'),
                         (43, 'Pounds', 'Kilograms'),
                         (44, 'Kilograms', 'Pounds'),

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
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}') 

elif conversion_number == 2:
    to_value = from_value * 1.8 + 32
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 3:
    to_value = from_value * 0.45
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 4:
    to_value = from_value * 2.22
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 5:
    to_value = from_value * 8
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}') 

elif conversion_number == 6:
    to_value = from_value / 8
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 7:
    to_value = (from_value *16)
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 8:
    to_value = (from_value /16)
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 9:
    to_value = (from_value /2)
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 10:
    to_value = (from_value *2)
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')    

elif conversion_number == 11:
    to_value = from_value * 48
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 12:
    to_value = from_value / 48
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 13:
    to_value = from_value / 4
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 14:
    to_value = from_value * 4
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 15:
    to_value = from_value / 16
    print(f'{from_value} {from_unit}  ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 16:
    to_value = from_value * 16
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 17:
    to_value = from_value * 3
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 18:
    to_value = from_value / 3
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 19:
    to_value = from_value / 2
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 20:
    to_value = from_value * 2
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 21:
    to_value = from_value / 16
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 22:
    to_value = from_value * 16
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 23:
    to_value = from_value / 14.787
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 24:
    to_value = from_value * 14.787
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 25:
    to_value = from_value * 29.574
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 26:
    to_value = from_value / 29.574
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 27:
    to_value = from_value * 240
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 28:
    to_value = from_value / 240
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 29:
    to_value = from_value * 4.167
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 30:
    to_value = from_value / 4.167
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 31:
    to_value = from_value * 2.113
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 32:
    to_value = from_value / 2.113
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 33:
    to_value = from_value * 1.057
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 34:
    to_value = from_value / 1.057
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 35:
    to_value = from_value / 3.785
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 36:
    to_value = from_value * 3.785
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 37:
    to_value = from_value / 28.35
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 38:
    to_value = from_value * 28.35
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 39:
    to_value = from_value / 453.6
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 40:
    to_value = from_value * 453.6
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 41:
    to_value = from_value / 16
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 42:
    to_value = from_value * 16
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 43:
    to_value = from_value / 2.205
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

elif conversion_number == 44:
    to_value = from_value * 2.205
    print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')