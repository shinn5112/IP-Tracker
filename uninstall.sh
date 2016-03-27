#!/usr/bin/env bash
# Author Patrick Shinn
# Version 1.0
# Uninstall Script
echo "You may wish to make a copy of your root crontab before running this."
echo "This program will remove all contents in the root crontab folder."
# Takes user input
read -p "Are you sure you wish to continue? yes/no: " answer

if [ $answer = "yes" ] # if the user answered yes, the uninstall will begin.
    then echo "Beginning uninstall process."

    else echo "Aborting."; exit  # Otherwise, the program terminates.
fi
echo "Changing directory to /opt"
cd /opt
sleep 2
echo "Removing root crontab"
sudo -S crontab -u root -r
sleep 2
echo "Removing WAN-Tracker program files"
sudo rm -r wan
sleep 2
echo "WAN-Tracker has been removed from your system."
sleep 2