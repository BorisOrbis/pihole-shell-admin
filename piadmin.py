#!/usr/bin/env python
#
#  Copyright (C) OrbisBoris <orbisboris@gmail.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License version 3 as
#   published by the Free Software Foundation.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#   Don't forget to run chmod +x piadmin.py before first use
#   PiHole Admin is used when the web admin is not working or tu shut down RPi
#   when starting use python3 piadmin.py or else python 2.7 will be default

# Import subprocess for sending commands to ssh bash
import subprocess
import time
import men as me
import clear_scr as cle
import os

subprocess.call(['clear'])  # calling command clear in bash
print(me.head)  # printing head and menu
print(me.menu)

# main loop
while True:
    try:
        lista = (["1", "2", "3", "4", "5", "6", "q", "r", "x", "v", "p", "g", "d", "e", "a", "u"])
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
        cle.end_clear()
    if op == '2':
        subprocess.call(['clear'])
        print('PiHole status...')
        subprocess.call(['pihole', 'status'])
        cle.end_clear()
    if op == '3':
        subprocess.call(['clear'])
        print('PiHole is restarting DNS...')
        subprocess.call(['pihole', 'restartdns'])
        cle.end_clear()
    if op == '4':
        subprocess.call(['clear'])
        print('PiHole debugging...')
        subprocess.call(['pihole', '-d'])
        cle.end_clear()
    if op == '5':
        subprocess.call(['clear'])
        print('PiHole chronometer...')
        subprocess.call(['pihole', '-c'])
        cle.end_clear()
    if op == '6':
        subprocess.call(['clear'])
        print('Flushing log...')
        subprocess.call(['pihole', '-f'])
        cle.end_clear()
    if op == 'r':
        subprocess.call(['clear'])
        print('RPi is going to restart.')
        cle.sure_reboot()
    if op == 'x':
        subprocess.call(['clear'])
        print('RPi is going to shut down.')
        cle.sure_shutdown()
    if op == 'a':
        subprocess.call(['clear'])
        print(me.about)
        cle.end_clear()
    if op == 'v':
        subprocess.call(['clear'])
        print('Pihole version...')
        subprocess.call(['pihole', '-v', '-c'])
        cle.end_clear()
    if op == 'p':
        subprocess.call(['clear'])
        print('Pihole change password...')
        pas = input('Please enter your new password: ')
        subprocess.call(['pihole', '-a', '-p', pas])
        cle.end_clear()
    if op == 'g':
        subprocess.call(['clear'])
        print('Pihole update Gravity...')
        subprocess.call(['pihole', 'updateGravity'])
        cle.end_clear()
    if op == 'e':
        subprocess.call(['clear'])
        print('Pihole enabling...')
        subprocess.call(['pihole', 'enable'])
        cle.end_clear()
    if op == 'd':
        subprocess.call(['clear'])
        print('Pihole disabling...')
        subprocess.call(['pihole', 'disable'])
        cle.end_clear()
    if op == 'u':
        subprocess.call(['clear'])
        print('Pihole disabling...')
        os.system('bash /home/pi/pihole-shell-admin/update.sh')  # update admin with update.sh
        cle.end_clear()
    if op == 'q':
        print('Thank you for using control panel and good bye!')
        time.sleep(3)
        subprocess.call(['clear'])
        break
# end of main loop
