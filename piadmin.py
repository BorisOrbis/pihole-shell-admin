#!/usr/bin/env python

#   Don't forget to run chmod +x piadmin.py before first use
#   PiHole Admin is used when the web admin is not working or tu shut down RPi
#   when starting use python3 piadmin.py or else python 2.7 will be default

#   Import subprocess for sending commands to ssh bash
import subprocess
import time
import men as me

#   Calling command clear in bash
subprocess.call(['clear'])

#   printing head and menu
print(me.head)
print(me.menu)
brisi = "'\e[3J'"
#   main loop
while True:
    try:
#   for only nambers change str to int
        lista = (["1", "2", "3", "4", "5","6", "q", "r", "x", "v", "p", "g", "d", "e", "a"])
        op = str(input('Please enter your selection: '))
    except ValueError:
        print('Sorry, your input is not correct.')
        continue
    if op not in lista:
        print('Sorry, your input is not correct pls. try again:')
        continue
    if op == '1':
        subprocess.call(['clear'])                                      # clear screen in terminal
        print('PiHole update started...')
        subprocess.call(['pihole', '-up'])                              # execute pihole -up in terminal
        input('Press enter to continue...')
        subprocess.call(['clear'])
        print(me.menu)
    if op == '2':
        subprocess.call(['clear'])
        print('PiHole status...')
        subprocess.call(['pihole', 'status'])
        input('Press enter to continue...')
        subprocess.call(['clear'])
        print(me.menu)
    if op == '3':
        subprocess.call(['clear'])
        print('PiHole is restarting DNS...')
        subprocess.call(['pihole', 'restartdns'])
        input('Press enter to continue...')
        subprocess.call(['clear'])
        print(me.menu)
    if op == '4':
        subprocess.call(['clear'])
        print('PiHole debuging...')
        subprocess.call(['pihole', '-d'])
        input('Press enter to continue...')
        subprocess.call(['clear'])
        print(me.menu)
    if op == '5':
        subprocess.call(['clear'])
        print('PiHole chronometar...')
        subprocess.call(['pihole', '-c'])
        input('Press enter to continue...')
        subprocess.call(['clear'])
        print(me.menu)
    if op == '6':
        subprocess.call(['clear'])
        print('Flushing log...')
        subprocess.call(['pihole', '-f'])
        input('Press enter to continue...')
        subprocess.call(['clear'])
        print(me.menu)
    if op == 'r':
        subprocess.call(['clear'])
        print('RPi is going to restart.')
        sigurnost = str(input('Are you shure (Y/n):'))
        if sigurnost == 'Y':
            print('RPi restarting...')
            subprocess.call(['sudo', 'reboot'])
        if sigurnost == 'y':
            print('Y must be capital')
            continue
        if sigurnost == 'n':
            subprocess.call(['clear'])
            print(me.menu)
    if op == 'x':
        subprocess.call(['clear'])
        print('RPi is going to shut down.')
        sigurnost = str(input('Are you shure (Y/n):'))
        if sigurnost == 'Y':
            print('RPi is shuting down...')
            subprocess.call(['sudo', 'halt'])
        if sigurnost == 'y':
            print('Y must be capital')
            continue
        if sigurnost == 'n':
            subprocess.call(['clear'])
            print(me.menu)
    if op == 'a':
        subprocess.call(['clear'])
        print(me.about)
        input('Press enter to continue...')
        subprocess.call(['clear'])
        print(me.menu)
    if op == 'v':
        subprocess.call(['clear'])
        print('Pihole version...')
        subprocess.call(['pihole', '-v', '-c'])
        input('Press enter to continue...')
        subprocess.call(['clear'])
        print(me.menu)
    if op == 'p':
        subprocess.call(['clear'])
        print('Pihole change pasword...')
        pas = input('Please enter your new pasword: ')
        subprocess.call(['pihole', '-a', '-p', pas])
        input('Press enter to continue...')
        subprocess.call(['clear'])
        print(me.menu)
    if op == 'g':
        subprocess.call(['clear'])
        print('Pihole update Gravity...')
        subprocess.call(['pihole', 'updateGravity'])
        input('Press enter to continue...')
        subprocess.call(['clear'])
        print(me.menu)
    if op == 'e':
        subprocess.call(['clear'])
        print('Pihole enabling...')
        subprocess.call(['pihole', 'enable'])
        input('Press enter to continue...')
        subprocess.call(['clear'])
        print(me.menu)
    if op == 'd':
        subprocess.call(['clear'])
        print('Pihole disabling...')
        subprocess.call(['pihole', 'disable'])
        input('Press enter to continue...')
        subprocess.call(['clear'])
        print(me.menu)
    if op == 'q':
        print('Thank you for using control panel and good bye!')
        time.sleep(3)
        subprocess.call(['clear'])
        break
#   end
