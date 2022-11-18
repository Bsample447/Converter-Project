print("\nWelcome to Brandon and Logan's Unit Converter Program\n") 
print("Below is a list of all possible conversions, please enter your request as")
print(":convert (Thing to change) (how many / much) to (thing to change it to)")


conversions_available = [('°f',             '°c'),
                         ('°c',             '°f'),
                         ('kilograms',      'pounds'), 
                         ('pounds',         'kilograms'),
                         ('cups',           'fluid-ounces'),
                         ('fluid-ounces',   'cups'),
                         ('cups',           'tablespoons'),
                         ('tbs',            'cups'),
                         ('cups',           'pints'),
                         ('pints',          'cups'),
                         ('cups',           'teaspoons' ),
                         ('teaspoons',      'cups'),
                         ('cups',           'quarts'),
                         ('quarts',         'cups'),
                         ('cups',           'gallons'),
                         ('gallons',        'cups'),
                         ('tablespoons',    'teaspoons'),
                         ('teaspoons',      'tablespoons'),
                         ('tablespoons',    'fluid-ounces'),
                         ('fluid-ounces',   'tablespoons'),
                         ('tablespoons',    'cups'),
                         ('cups',           'tablespoons'),
                         ('milliliters',    'tablespoons'),
                         ('tablespoons',    'milliliters'),
                         ('milliliters',    'fluid-ounces'),
                         ('fluid-ounces',   'milliliters'),
                         ('cups',           'millilters'),
                         ('milliliters',    'cups'),
                         ('liters',         'cups'),
                         ('cups',           'liters'),
                         ('liters',         'pints'),
                         ('pints',          'liters'),
                         ('liters',         'quarts'),
                         ('quarts',         'liters'),
                         ('liters',         'gallons'),
                         ('gallons',        'liters'),
                         ('ounces',         'grams'),
                         ('grams',          'ounces'),
                         ('grams',          'pounds'),
                         ('pounds',         'grams'),
                         ('pounds',         'ounces'),
                         ('onces',          'pounds'),
                         ('quarts',         'gallons'),
                         ('gallons',        'quarts'),

]

print("Available Conversions\n")
index = 1
for from_unit, to_unit in conversions_available:
    print('{:2d}) {:14s} -> {}'.format(index,from_unit,to_unit))
    index += 1

def convert_units(unitIn):
    unitOut = unitIn
    if unitIn == 'f' or unitIn == 'fahrenheit' or unitIn == 'F':
        unitOut = '°f'
    elif unitIn =='c' or unitIn == 'celsius'or unitIn =='C':
        unitOut = '°c'
    elif unitIn == 'kilo' or unitIn == 'kg' or unitIn == 'KG' or unitIn == 'kg' or unitIn == 'kilos' or unitIn == 'kilograms':
        unitOut = 'kilograms'
    elif unitIn == 'lbs' or unitIn == 'pounds' or unitIn == 'pound'or  unitIn == 'lb':
        unitOut = 'pounds'
    elif unitIn == 'cups' or unitIn == 'cup' or unitIn == 'cp' or unitIn == 'cps':
        unitOut = 'cups'
    elif unitIn == 'floz' or unitIn == 'fluidoz' or unitIn == 'fluid ounces':
        unitOut = 'fluid-ounces'
    elif unitIn == 'tbs' or unitIn == 'Tbs' or unitIn == 'Tablespoons' or unitIn == 'tb' or unitIn == 'tablespoon':
        unitOut = 'tablespoons'
    elif unitIn == 'pints' or unitIn == 'pt' or unitIn == 'pts' or unitIn == 'pint':
        unitOut = 'pints'
    elif unitIn == 'tsp' or unitIn == 'teaspoons' or unitIn == 'teaspoon':
        unitOut = 'teaspoons'
    elif unitIn == 'quarts' or unitIn == 'qts' or unitIn == 'quart' or unitIn == 'quarts':
        unitOut = 'quarts'
    elif unitIn == 'gallons' or unitIn == 'gal' or unitIn == 'Gallons' or unitIn == 'gals':
        unitOut = 'gallons'
    elif unitIn == 'ml' or unitIn == 'milliliters' or unitIn == 'mls' or unitIn == 'milliliter':
        unitOut = 'milliliters'
    elif unitIn == 'liters' or unitIn == 'lt' or unitIn == 'lts' or unitIn == 'liter':
        unitOut = 'liters'
    elif unitIn == 'grams' or unitIn == 'g' or unitIn == 'gs' or unitIn =='gram':
        unitOut = 'grams'
    elif unitIn == 'ounces' or unitIn == 'oz' or unitIn == 'ounce':
        unitOut = 'ounces'


    return unitOut
    
    
print()
while(True):
    conversion = input('What would you like to convert? (enter q to quit) --> ')
    if conversion == 'q':
        exit()
    conversion = conversion.split()
    try: 


        from_unit = conversion[2].lower()
        from_value = float(conversion[1])
        to_unit = conversion[4].lower()

        from_unit = convert_units(from_unit)
        to_unit   = convert_units(to_unit)

        conversion = conversions_available.index((from_unit, to_unit))+1
    except: print("Invalid Input, Please use syntax like 'convert 32 f to c' and use proper measurements terminology and abbreviations" )

    
   
    
    if conversion == 1:
        to_value = (from_value - 32) / 1.8
        print(f'{from_value} {from_unit} ( Is Equal to ) -> {to_value} {to_unit}') 

    elif conversion == 2:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value*1.8 + 32, to_unit))

    elif conversion == 3:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value* 2.2205, to_unit))

    elif conversion == 4:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/ 2.2205, to_unit))

    elif conversion == 5:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value* 8.115, to_unit))

    elif conversion == 6:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/ 8.115, to_unit))

    elif conversion == 7:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value* 16, to_unit))

    elif conversion == 8:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/ 8, to_unit))

    elif conversion == 9:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/ 2, to_unit))

    elif conversion == 10:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value* 2, to_unit)) 

    elif conversion == 11:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value* 48, to_unit))

    elif conversion == 12:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/ 48, to_unit))

    elif conversion == 13:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/4, to_unit))

    elif conversion == 14:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value* 4, to_unit))

    elif conversion == 15:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/ 16, to_unit))

    elif conversion == 16:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value *16, to_unit))

    elif conversion == 17:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value *3, to_unit))

    elif conversion == 18:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value /3, to_unit))

    elif conversion == 19:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/ 2, to_unit))

    elif conversion == 20:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value * 2, to_unit))

    elif conversion == 21:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/ 16, to_unit))

    elif conversion == 22:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value* 16, to_unit))

    elif conversion == 23:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/ 14.787, to_unit))

    elif conversion == 24:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value * 14.787, to_unit))

    elif conversion == 25:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value* 29.574, to_unit))

    elif conversion == 26:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/ 29.574, to_unit))

    elif conversion == 27:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value*240, to_unit))

    elif conversion == 28:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/ 240, to_unit))

    elif conversion == 29:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value*4.167, to_unit))

    elif conversion == 30:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/ 4.167, to_unit))

    elif conversion == 31:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value*2.113, to_unit))

    elif conversion == 32:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/ 2.113, to_unit))

    elif conversion == 33:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value*1.057, to_unit))

    elif conversion == 34:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/1.057, to_unit))

    elif conversion == 35:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value /3.785, to_unit))

    elif conversion == 36:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value*3.785, to_unit))

    elif conversion == 37:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/28.35, to_unit))

    elif conversion == 38:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value*28.35, to_unit))

    elif conversion == 39:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/453.6, to_unit))

    elif conversion == 40:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value*453.6, to_unit))

    elif conversion == 41:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/16, to_unit))

    elif conversion == 42:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value*16, to_unit))

    elif conversion == 43:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/4, to_unit))

    elif conversion == 44:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value*4, to_unit))
    