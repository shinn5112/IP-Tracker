#!/usr/bin/env bash
# WAN-Tracker update script
# Author Patrick Shinn
# Version 2.0
# Last updated 3/27/16
echo "Updating WAN_Checker.py and Setup.py to the newest version: pulling from GitHub"
# creates a tmp file for output and a tmp file for errors
git pull > tmp 2> tmp.error
# checks tmp file to see if already up to date, if so, exit
update=$( tail tmp | grep "Already up-to-date.")
if [[ $update == "Already up-to-date." ]]
then echo $update; rm tmp tmp.error; sleep 1; exit
fi

# checks error file to see if connecting to server failed, if not, begin update, otherwise exit
update=$(tail tmp.error | grep "fatal: Could not read from remote repository.")
if [[ $update == "fatal: Could not read from remote repository." ]]
then echo "Could not reach the repository, please check your internet connection and try again."; rm tmp tmp.error; sleep 1; exit
else echo "Update found, updating to newest version."
fi
# remove unnecessary tmp files, and update the software.
rm tmp tmp.error
sudo -S cp -vf Setup.py WAN_Checker.py /opt/wan
echo "Updating WAN_Checker.py and Setup.py to the newest version."
cd /opt/wan
sudo chmod +x Setup.py WAN_Checker.py
sudo chown root:root Setup.py WAN_Checker.py
sudo chmod 700 Setup.py WAN_Checker.py
sleep 2
# Makes the software send a confirmation email once update is finished on next run.
echo -n "Writing on status to status file: changing from 0 to "
sudo echo -n "1" | sudo tee status.txt
echo ""
sleep 2
echo "Update complete, please check your recipient email in two minutes or so to confirm."
sleep 2