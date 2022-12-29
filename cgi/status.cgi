#!/bin/sh -xv
echo "Content-type: application/json"
echo ""
cmcontrol --get-guest-list-json
