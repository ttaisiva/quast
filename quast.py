from data import *
from unit_converter.converter import convert
#Data size, time, distance, mass and temperatures are supported.
# unit conversion for more advanced units
def quast_convert(args):
    for key in conversion_factors:
        s = args[1]+args[2]
        if s == key: # convert from smaller to bigger unit
            return (float)(args[0])/conversion_factors[key]
        s = args[2]+args[1] #reverse string
        if s == key: # convert from bigger to smaller unit
            return (float)(args[0])*conversion_factors[key]

def unit(args):
    # check for argument formatting
    try:
        val = (float)(args[0])
    except:
        print('>>> Arguments are <value> <unit1> <unit2>. First argument must be a number.')
        return
    # check for existing conversions
    try:
        # adjust temperature units for library function
        if args[1] in alt_units.keys(): 
            args[1] = alt_units[args[1]]
        if args[2] in alt_units.keys():
            args[2] = alt_units[args[2]]
        result = convert(args[0]+' '+args[1], args[2])
        result = '{:.2f}'.format((result)) + ' ' + args[2]
    except:
        for key in units:
            if args[1] in units[key]:
                if not args[2] in units[key]:
                    print('Incompatible unit types: '+args[1]+\
                          ' must be converted to another '+key+' unit.')
                    return
                else:
                    result = quast_convert(args)
                    result = '{:.3e}'.format((result)) + ' ' + args[2]
    print('>>> ' + str(result))

def quit():
    print('>>> Quitting Quast.')
    exit()

def sphere(args):
    r = (float)(args[0])
    print('Surface Area: '+'{:.3e}'.format(4*math.pi*r**2)+' '+args[1]+\
          '\nVolume: '+'{:.3e}'.format(4/3*math.pi*r**3)+' '+args[1])

def const(arg):
    for list in names:
        if arg in list:
            key = list[0]
            print(key+': ' + constants[key])
            return
    print('Constant not found. (Symbols are case sensitive.)')
    
# validate number of arguments based on command
def valid_arg_cnt(n, userin):
    if len(userin)!=n:
        print('>>> Invalid number of arguments.')
    return len(userin)==n

def quast():
    userin = input('>>> ')
    cmd = userin.split()[0].lower()
    if(cmd == 'help'):
        print(help_msg)
    elif(cmd == 'unit'):
        if not valid_arg_cnt(4, userin.split()):
            return
        unit(userin.split()[1:])
    elif(cmd == 'const'):
        const(userin[6:])
    elif(cmd == 'sun'):
        print(sun_info)
    elif(cmd == 'sphere'):
        if not valid_arg_cnt(3, userin.split()):
            return
        sphere(userin.split()[1:])
    elif(cmd == 'quit'):
        quit()
    else:
        print('>>> Invalid command.')
    return

# entry point
print('\nWelcome to Quast - Quick Astronomy tools at your fingertips!\n\
       Type "help" to see a list of commands.\n')
while(True):
    quast()


    