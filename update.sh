#!/usr/bin/env bash
# WAN-Tracker update script
# Author Patrick Shinn
# Version 2.0
# Last updated 3/27/16
echo "Updating WAN_Checker.py and Setup.py to the newest version: pulling from GitHub"
git pull > tmp 2> tmp.error
update=$( tail tmp | grep "Already up-to-date.")
if [[ $update == "Already up-to-date." ]]
then echo $update; rm tmp tmp.error; exit
fi
update=$(tail tmp.error | grep "fatal: Could not read from remote repository.")
if [[ $update == "fatal: Could not read from remote repository." ]]
then echo "Could not reach the repository, please check your internet connection and try again."; rm tmp tmp.error; exit
else echo "Update found, updating to newest version."
fi
rm tmp tmp.error
sudo -S cp -vf Setup.py WAN_Checker.py /opt/wan
echo "Updating WAN_Checker.py and Setup.py to the newest version."
cd /opt/wan
sudo chmod +x Setup.py WAN_Checker.py
sudo chown root:root Setup.py WAN_Checker.py
sudo chmod 700 Setup.py WAN_Checker.py
echo -n "Writing on status to status file: changing from 0 to "
sudo echo -n "1" | sudo tee status.txt
echo ""
echo "Update complete, please check your recipient email in two minutes or so to confirm."
sleep 2