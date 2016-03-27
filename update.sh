#!/usr/bin/env bash
# WAN-Tracker update script
#  Author Patrick Shinn
# Version 1.0
# Last updated 3/27/16
echo "Updating WAN_Checker.py and Setup.py to the newest version: pulling from GitHub"
git pull
sudo -S mv -vf Setup.py WAN_Checker.py /opt/wan
echo "Updating WAN_Checker.py and Setup.py to the newest version."
sudo chmod +x Setup.py WAN_Checker.py
sudo chown root:root Setup.py WAN_Checker.py
sudo chmod 700 Setup.py WAN_Checker.py
sleep 2
echo "Update complete, please check your recipient email in two minutes or so to confirm."
sleep 2