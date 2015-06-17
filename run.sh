#!/bin/sh
set -e

# Fill in TOKEN with GitHub API Token
GHTOKEN=
# FIll in WWWPATH with the destination path of static html
WWWPATH=

source ./env/bin/activate
./bin/issues -t $TOKEN -r helium/router -r helium/engineering -r helium/snapboard -r helium/embedded json -o out.json
./bin/generate_html out.json $WWWPATH
