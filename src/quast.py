from data import *
from unit_converter.converter import convert

def unit(args):
    # check for argument formatting
    try:
        val = (float)(args[0])
    except:
        print('>>> Arguments are <value> <unit1> <unit2>. First argument must be a number.')
        return
    # check for existing conversions
    try:
        result = convert(args[0]+' '+args[1], args[2])
        print('>>> ' + str(result) + ' ' + args[2]) # temp
    except:
        print('do own unit conversion')
    # print('>>> ' + str(result) + ' ' + args[2])
    

def quit():
    print('>>> Quitting Quast.')
    exit()

# validate number of arguments based on command
def valid_arg_cnt(cmd, userin):
    if cmd == 'unit':
        return len(userin)==4
    elif cmd == 'const':
        return len(userin)==2
    elif cmd == 'sphere':
        return len(userin)==3
    else: #cmd is mainseq
        return len(userin)==3

def quast():
    userin = input('>>> ')
    cmd = userin.split()[0].lower()
    if(cmd == 'help'):
        print(help_msg)
    elif(cmd == 'unit'):
        if not valid_arg_cnt(cmd, userin.split()):
            print('>>> Invalid number of arguments.')
            return
        unit(userin.split()[1:])
    elif(cmd == 'sun'):
        print(sun_info)
    elif(cmd == 'quit'):
        quit()
    else:
        print('>>> Invalid command.')
    return

print('\nWelcome to Quast - Quick Astronomy tools at your fingertips!\n\
       Type "help" to see a list of commands.\n')
while(True):
    quast()


    