from data import *

def quit():
    print('>>> Quitting Quast.')
    exit()

# validate number of arguments based on command
def valid_arg_cnt(cmd, userin):
    print(userin)

def quast():
    userin = input('>>> ')
    cmd = userin.split()[0].lower()
    if(cmd == valid_commands[0]):
        print(help_msg)
    elif(cmd == valid_commands[1]):
        valid_arg_cnt(cmd, userin.split().lower)
    elif(cmd == valid_commands[3]):
        print(sun_info)
    elif(cmd == valid_commands[6]):
        quit()
    else:
        print('>>> Invalid command.')
    return

print('\nWelcome to Quast - Quick Astronomy tools at your fingertips!\n\
       Type "help" to see a list of commands.\n')
while(True):
    quast()


    