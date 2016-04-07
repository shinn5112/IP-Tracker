#!/usr/bin/env bash
VAR=$(pwd)
echo $VAR
echo "Installing auto-update crontab.";echo -n "* * * * * "; echo -n $VAR; echo " 2>> /opt/wan/updateErrorLog.txt"
