#!/bin/sh -xv
echo "Content-type: text/plain"
echo ""
cmcontrol --change-active-guest-name=agl-html5-ivi-demo
cmcontrol --shutdown-guest-role=ivi
echo "Status: 200"
