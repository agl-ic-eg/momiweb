#!/bin/sh -xv
echo "Content-type: text/plain"
echo ""
cmcontrol --change-active-guest-name=agl-momi-ivi-demo
cmcontrol --shutdown-guest-role=ivi
echo "Status: 200"
