#!/usr/bin/env bash
# WAN-Tracker update script
# Author Patrick Shinn
# Version 1.0
# Last updated 4/8/16

# creates a tmp file for output and a tmp file for errors
localRepo=$(cat /opt/wan/pwd.txt)
cd $localRepo
git pull > tmp 2> tmp.error
# checks tmp file to see if already up to date, if so, exit
update=$( tail tmp | grep "Already up-to-date.")
if [[ $update == "Already up-to-date." ]]
then rm tmp tmp.error;  exit
fi

# checks error file to see if connecting to server failed, if not, begin update, otherwise exit
update=$(tail tmp.error | grep "fatal: Could not read from remote repository.")
if [[ $update == "fatal: Could not read from remote repository." ]]
then  rm tmp tmp.error; echo $update >> /opt/wan/updateErrorLog.txt; exit
else (echo -n "Software update found, updating on: "; echo $(date)) >> /opt/wan/updateLog.txt
fi
# remove unnecessary tmp files, and update the software.
rm tmp tmp.error

cp -vf Setup.py WAN_Checker.py /opt/wan
cd /opt/wan
chmod +x Setup.py WAN_Checker.py
chown root:root Setup.py WAN_Checker.py
chmod 700 Setup.py WAN_Checker.py