#!/bin/sh -xv
echo "Content-type: text/html"
cmcontrol --change-active-guest-name=agl-momi-ivi-demo-res
cmcontrol --shutdown-guest-role=ivi
echo "Status: 200"
