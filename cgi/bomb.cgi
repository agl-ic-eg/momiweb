#!/bin/sh -xv
echo "Content-type: text/html"
cmcontrol --force-reboot-guest-role=ivi && echo "Status: 200"
