# Functions for clearing screen of shell 'end_clear'
# and for Y/n choosing on the end of the program
# used in piadmin.py.

import subprocess
import men as me


sig = str  # declare sig and pro as strings
pro = str


def up_date():
    update = subprocess.call(['bash', '/home/pi/pihole-shell-admin/update.sh'])  # update admin with update.sh
    if update == 0:
        print('Update successful...')
    else:
        print('Something went wrong pls. try later...')


def end_clear():
    input('Press enter to continue...')
    subprocess.call(['clear'])
    print(me.menu)


def sure_reboot():
    while True:  # Yes or no loop
        try:
            pro = (["Y", "n"])
            sig = str(input('Are you sure (Y/n)'))
        except ValueError:
            print('Sorry, your input is not correct.')
        if sig not in pro:
            print('Please input Y ili n')
        if sig == 'Y':
            print('RPi restarting...')
            subprocess.call(['sudo', 'reboot'])
        if sig == 'n':
            subprocess.call(['clear'])
            print(me.menu)
            break


def sure_shutdown():
    while True:
        try:
            pro = (["Y", "n"])
            sig = str(input('Are you sure (Y/n)'))
        except ValueError:
            print('Sorry, your input is not correct.')
        if sig not in pro:
            print('Please input Y ili n')
        if sig == 'Y':
            print('RPi is shouting down...')
            subprocess.call(['sudo', 'halt'])
        if sig == 'n':
            subprocess.call(['clear'])
            print(me.menu)
            break
