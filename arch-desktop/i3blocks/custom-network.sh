#!/bin/bash

case $BLOCK_BUTTON in
    1) i3-msg 'workspace 9; exec alacritty -e nmtui'
esac


SSID=$(iwgetid --raw)

if [ -z "$SSID" ]; then
    echo "NO CONNECTION"
    echo "NO CONNECTION"

else
    echo "$SSID"
    echo "$SSID"
fi

