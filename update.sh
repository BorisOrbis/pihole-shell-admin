#!/bin/bash
rm -rdf /home/pi/pihole-shell-admin
cd /home/pi/pihole-shell-admin && git reset --hard &&  git pull "https://github.com/BorisOrbis/pihole-shell-admin.git"
