#!/bin/bash

# This script creates Siegfried signatures from the custom
# DROID signatures in this directory. After build they will
# replace the default signatures. To revert to the original
# signatures afterwards, manually run "sudo roy build"

sudo cp *.xml /usr/share/siegfried/
sudo roy build -noreports \
     -droid /usr/share/siegfried/apk-standard-base.xml \
     -container /usr/share/siegfried/apk-container-base.xml