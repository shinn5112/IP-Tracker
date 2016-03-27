#!/usr/bin/env bash
# WAN-Tracker update script
#  Author Patrick Shinn
# Version 2.0
# Last updated 3/27/16
echo "Updating WAN_Checker.py and Setup.py to the newest version: pulling from GitHub"
git pull > tmp
update=$( tail tmp | grep "Already up-to-date.")
if [[ $update == "Already up-to-date." ]]
then echo $update; rm tmp; exit
fi
update=$(tail tmp | grep "Could not read from remote repository.")
if [[ $update == "Could not read from remote repository." ]]
then echo "Could not reach the repository, please check your internet connection and try again."; rm tmp; exit

else echo "Update found, updating to newest version."
fi
rm tmp

