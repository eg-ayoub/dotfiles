#!/bin/bash

here="$(dirname $0)"
source "$here/common.sh"

autorandr -c & \
run variety & \
run nm-applet & \
sleep 5 && run volumeicon -d default & disown & \
run xfce4-clipman &
