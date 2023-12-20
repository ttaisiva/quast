from data import *

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
        print('ok args')
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


    