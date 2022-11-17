print()
print("Welcome to Brandon and Logan's Unit Converter Program")
print()
#Test Please

conversions_available = [('°F', '°C'),
                         ('°C', '°F'),
                         ('kg', 'lbs'),
                         ('lbs', 'kg'),
                         ('cups', 'fluid-ounces'),
                         ('fluid-ounces',  'cups'),
                         ('cups', 'tbs'),
                         ('Tbs',  'ups'),
                         ('Cups',  'Pint'),
                         ('Pint', 'Cups'),
                         ('Cups', 'Teaspoons' ),
                         ('Teaspoons', 'Cups'),
                         ('Cups', 'Quarts'),
                         ('Quarts', 'Cups'),
                         ('Cups', 'Gallons'),
                         ('Gallons', 'Cups'),
                         ('Tablespoons', 'Teaspoons'),
                         ('Teaspoons', 'Tablespoons'),
                         ('Tablespoons', 'FlOunces'),
                         ('FlOunces', 'Tablespoons'),
                         ('Tablespoons', 'Cups'),
                         ('Cups', 'Tablespoons'),
                         ('Milliliters', 'Tablespoons'),
                         ('Tablespoons', 'Milliliters'),
                         ('Milliliters', 'Fl-Ounces'),
                         ('Fl-Ounces', 'Milliliters'),
                         ('Cups', 'Millilters'),
                         ('Milliliters', 'Cups'),
                         ('Liters', 'Cups'),
                         ('Cups', 'Liters'),
                         ('Liters', 'Pints'),
                         ('Pints', 'Liters'),
                         ('Liters', 'Quarts'),
                         ('Quarts', 'Liters'),
                         ('Liters', 'Gallons'),
                         ('Gallons', 'Liters'),
                         ('Grams','Ounces'),
                         ('Grams', 'Ounces'),
                         ('Grams', 'Pounds'),
                         ('Pounds', 'Grams'),
                         ('Pounds', 'Ounces'),
                         ('Ounces', 'Pounds'),
                         ('Pounds', 'Kilograms'),
                         ('Kilograms', 'Pounds'),

]

print("Available Conversions\n")
index = 1
for from_unit, to_unit in conversions_available:
    print('{:2d}) {:14s} -> {}'.format(index,from_unit,to_unit))
    index += 1
    
print()
while(True):
    conversion = input('Enter the number of the conversion to use (enter -1 to exit) --> ')
    conversion =int(conversion) - 1
    if conversion < 0:
        exit()

    from_unit, to_unit = conversions_available[conversion]
    print()
    from_value = float(input(f'Enter {from_unit} --> ' ))
    print()

    
    if conversion == 1:
        to_value = (from_value - 32) / 1.8
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}') 

    elif conversion == 2:
        to_value = from_value * 1.8 + 32
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 3:
        to_value = from_value * 0.45
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 4:
        to_value = from_value * 2.22
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 5:
        to_value = from_value * 8
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}') 

    elif conversion == 6:
        to_value = from_value / 8
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 7:
        to_value = (from_value *16)
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 8:
        to_value = (from_value /16)
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 9:
        to_value = (from_value /2)
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 10:
        to_value = (from_value *2)
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')    

    elif conversion == 11:
        to_value = from_value * 48
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 12:
        to_value = from_value / 48
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 13:
        to_value = from_value / 4
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 14:
        to_value = from_value * 4
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 15:
        to_value = from_value / 16
        print(f'{from_value} {from_unit}  ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 16:
        to_value = from_value * 16
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 17:
        to_value = from_value * 3
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 18:
        to_value = from_value / 3
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 19:
        to_value = from_value / 2
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 20:
        to_value = from_value * 2
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 21:
        to_value = from_value / 16
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 22:
        to_value = from_value * 16
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 23:
        to_value = from_value / 14.787
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 24:
        to_value = from_value * 14.787
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 25:
        to_value = from_value * 29.574
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 26:
        to_value = from_value / 29.574
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 27:
        to_value = from_value * 240
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 28:
        to_value = from_value / 240
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 29:
        to_value = from_value * 4.167
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 30:
        to_value = from_value / 4.167
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 31:
        to_value = from_value * 2.113
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 32:
        to_value = from_value / 2.113
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 33:
        to_value = from_value * 1.057
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 34:
        to_value = from_value / 1.057
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 35:
        to_value = from_value / 3.785
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 36:
        to_value = from_value * 3.785
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 37:
        to_value = from_value / 28.35
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 38:
        to_value = from_value * 28.35
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 39:
        to_value = from_value / 453.6
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}')

    elif conversion == 40:
       print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value*453.6, to_unit))

    elif conversion == 41:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/16, to_unit))

    elif conversion == 42:
       print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value*16, to_unit))

    elif conversion == 43:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/2.205, to_unit))

    elif conversion == 44:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value*2.205, to_unit))