from data import *
from unit_converter.converter import convert

# unit conversion for more advanced units
def quast_convert(args):
    for key in conversion_factors:
        s = args[1]+args[2]
        if s == key: # convert from smaller to bigger unit
            return (float)(args[0])/conversion_factors[key]
        s = args[2]+args[1] #reverse string
        if s == key: # convert from bigger to smaller unit
            return (float)(args[0])*conversion_factors[key]

def unit(args): #incomplete
    # check for argument formatting
    try:
        val = (float)(args[0])
    except:
        print('>>> Arguments are <value> <unit1> <unit2>. First argument must be a number.')
        return
    # check for existing conversions
    try:
        result = convert(args[0]+' '+args[1], args[2])
    except:
        for key in units:
            if args[1] in units[key]:
                if not args[2] in units[key]:
                    print('Incompatible unit types: '+args[1]+\
                          ' must be converted to another '+key+' unit.')
                    return
                else:
                    result = quast_convert(args)
    print('>>> ' + '{:.3e}'.format((result)) + ' ' + args[2])

def quit():
    print('>>> Quitting Quast.')
    exit()

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
        if not valid_arg_cnt(2, userin.split()):
            return
    elif(cmd == 'sun'):
        print(sun_info)
    elif(cmd == 'sphere'):
        if not valid_arg_cnt(3, userin.split()):
            return
    elif(cmd == 'prefix'):
        print('prefix table')
    elif(cmd == 'quit'):
        quit()
    else:
        print('>>> Invalid command.')
    return

print('\nWelcome to Quast - Quick Astronomy tools at your fingertips!\n\
       Type "help" to see a list of commands.\n')
while(True):
    quast()


    