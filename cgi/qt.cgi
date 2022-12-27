#!/bin/sh -xv
echo "Content-type: text/html"
cmcontrol --change-active-guest-name=agl-qt-ivi-demo
cmcontrol --shutdown-guest-role=ivi
echo "Status: 200"
