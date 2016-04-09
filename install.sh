#!/usr/bin/env bash
# WAN-Tracker install script
# Author Patrick Shinn
# Version 2.0
# Last updated 4/8/16

# saves github repo clone directory for crontab installation for auto-update.
localRepo=$(pwd)

# saves github repo clone directory for auto-update usage.
sudo echo $localRepo > pwd.txt

# Begin program
echo "Thank you for installing WAN-Tracker. Your install will begin soon."
echo "Please ensure that you have Python 3 installed before executing this script."

# makes a wan directory in the optional software folder, then places a copy of setup, pwd.txt, and WAN_Checker in it.
sudo -S mkdir -v /opt/wan
echo "Moving files to /opt/wan folder."
sudo cp -v Setup.py WAN_Checker.py pwd.txt /opt/wan
cd /opt/wan
# Changes to the new wan directory, and secures the program files
sudo chown root:root Setup.py WAN_Checker.py pwd.txt
sudo chmod 644 pwd.txt
sudo chmod +x Setup.py WAN_Checker.py
sudo chmod 700 Setup.py WAN_Checker.py
sleep 3
echo "Starting setup program, please use Easy setup if you are a first time user."
sleep 4
# clears the screen, then runs the setup.py script
clear
sudo ./Setup.py
clear
# clears the screen after exiting setup and then secures the generated files.  The installs automation crontab.
echo "Securing settings files"
sleep 2
sudo chown root:root settings.txt log.txt status.txt wan.txt
sudo chmod 700 settings.txt
sudo touch errorlog.txt
sudo chmod 744 log.txt status.txt wan.txt wan.txt errorlog.txt
sudo chmod -x settings.txt log.txt status.txt wan.txt errorlog.txt
echo "Installing crontab for automation under root."
sleep 2
echo "* * * * * python3 /opt/wan/WAN_Checker.py 2>> /opt/wan/errorlog.txt" | sudo crontab -u root -

# Auto-update install and setup.
read -p "Would you like to receive automatic updates? y/N: " answer
if [[ $answer == "y" ]]
then echo "Installing auto-update crontab."; (sudo -S crontab -u root -l; echo -n "0 0 * * * "; echo -n $localRepo; echo "/auto-update.sh 2>> /opt/wan/updateErrorLog.txt") | sudo crontab -u root -; sudo touch updateErrorLog.txt updateLog.txt; sudo chown root:root updateErrorLog.txt updateLog.txt; sudo chmod 744 updateErrorLog.txt updateLog.txt; sudo chmod -x updateErrorLog.txt updateLog.txt; echo "Auto updates enabled."
fi

# Ends installation, prints a messages to the user letting them know.
echo "Install complete. Please check your designated recipient email in two minutes or so."
sleep 4