#!/bin/sh

UPSTREAM=${1:-'@{u}'}
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse "$UPSTREAM")
BASE=$(git merge-base @ "$UPSTREAM")

if [ $LOCAL = $REMOTE ]; then
    echo "Up-to-date"
elif [ $LOCAL = $BASE ]; then
    echo "Need to pull"
    cd /home/pi/pihole-shell-admin && git reset --hard && git pull "https://github.com/BorisOrbis/pihole-shell-admin.git" &>/dev/null
#elif [ $REMOTE = $BASE ]; then
#    echo "Need to push"
else
    echo "Error...try again."
fi
