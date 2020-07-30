#!/usr/bin/env bash

function run {
  if ! pgrep -f $1 ;
  then
    $@&
  fi
}

run xrandr --output HDMI-A-0 --primary
run xrandr --output HDMI-A-0 --left-of DVI-D-0
run xrandr --output DisplayPort-0 --above HDMI-A-0
run compton
run nm-applet
run blueman-applet
run xfce4-power-manager
