#!/bin/sh -xv
echo "Content-type: text/html"
cmcontrol --change-active-guest-name=agl-flutter-ivi-demo
cmcontrol --shutdown-guest-role=ivi
echo "Status: 200"
