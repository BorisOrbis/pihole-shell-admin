#!/usr/bin/env python

#   Don't forget to run chmod +x piadmin.py before first use
#   PiHole Admin is used when the web admin is not working or tu shut down RPi
#   when starting use python3 piadmin.py or else python 2.7 will be default

# Import subprocess for sending commands to ssh bash
import subprocess
import time
import men as me

subprocess.call(['clear'])  # Calling command clear in bash

# printing head and menu
print(me.head)
print(me.menu)
brisi = "'\e[3J'"  # insert '\e[3J' to clear video memory

sig = str  # declare sig and pro as strings
pro = str

def end_clear():
    input('Press enter to continue...')
    subprocess.call(['clear'])
    print(me.menu)

# main loop
while True:
    try:
# for only numbers change str to int
        lista = (["1", "2", "3", "4", "5","6", "q", "r", "x", "v", "p", "g", "d", "e", "a"])
        op = str(input('Please enter your selection: '))
    except ValueError:
        print('Sorry, your input is not correct.')
        continue
    if op not in lista:
        print('Sorry, your input is not correct pls. try again:')
        continue
    if op == '1':
        subprocess.call(['clear'])  # clear screen in terminal
        print('PiHole update started...')
        subprocess.call(['pihole', '-up'])  # execute pihole -up in terminal
        end_clear()
    if op == '2':
        subprocess.call(['clear'])
        print('PiHole status...')
        subprocess.call(['pihole', 'status'])
        end_clear()
    if op == '3':
        subprocess.call(['clear'])
        print('PiHole is restarting DNS...')
        subprocess.call(['pihole', 'restartdns'])
        end_clear()
    if op == '4':
        subprocess.call(['clear'])
        print('PiHole debuging...')
        subprocess.call(['pihole', '-d'])
        end_clear()
    if op == '5':
        subprocess.call(['clear'])
        print('PiHole chronometar...')
        subprocess.call(['pihole', '-c'])
        end_clear()
    if op == '6':
        subprocess.call(['clear'])
        print('Flushing log...')
        subprocess.call(['pihole', '-f'])
        end_clear()
    if op == 'r':
        subprocess.call(['clear'])
        print('RPi is going to restart.')
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
    if op == 'x':
        subprocess.call(['clear'])
        print('RPi is going to shut down.')
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
    if op == 'a':
        subprocess.call(['clear'])
        print(me.about)
        end_clear()
    if op == 'v':
        subprocess.call(['clear'])
        print('Pihole version...')
        subprocess.call(['pihole', '-v', '-c'])
        end_clear()
    if op == 'p':
        subprocess.call(['clear'])
        print('Pihole change pasword...')
        pas = input('Please enter your new pasword: ')
        subprocess.call(['pihole', '-a', '-p', pas])
        end_clear()
    if op == 'g':
        subprocess.call(['clear'])
        print('Pihole update Gravity...')
        subprocess.call(['pihole', 'updateGravity'])
        end_clear()
    if op == 'e':
        subprocess.call(['clear'])
        print('Pihole enabling...')
        subprocess.call(['pihole', 'enable'])
        end_clear()
    if op == 'd':
        subprocess.call(['clear'])
        print('Pihole disabling...')
        subprocess.call(['pihole', 'disable'])
        end_clear()
    if op == 'q':
        print('Thank you for using control panel and good bye!')
        time.sleep(3)
        subprocess.call(['clear'])
        break
# end of main loop
