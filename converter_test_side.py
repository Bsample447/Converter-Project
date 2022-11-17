
print("\nWelcome to Brandon and Logan's Unit Converter Program\n") 
print("Below is a list of all possible conversions, please enter your request as")
print(":convert (thing 1) to (thing 2)")


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

def convert_units(unitIn):
    unitOut = unitIn
    if unitIn == 'f' or unitIn == 'fahrenheit':
        unitOut = '°F'
    elif unitIn =='c' or unitIn == 'celsius':
        unitOut = '°C'
    

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
    except: print("Invalid Input, Please use syntax like 'convert 32 f to c'" )

    
    
    if conversion == 1:
      print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value-32 / 1.8, to_unit))

    elif conversion == 2:
      print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value *1.8 + 32, to_unit))

    elif conversion == 3:
      print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value* 0.45, to_unit))

    elif conversion == 4:
      print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value*2.22, to_unit))

    elif conversion == 5:
      print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value* 8, to_unit))

    elif conversion == 6:
      print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/ 8, to_unit))

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
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value/2.205, to_unit))

    elif conversion == 44:
        print('{} {} ( Is Equal to ) -> {:.2f} {}'.format(from_value, from_unit, from_value*2.205, to_unit))

  