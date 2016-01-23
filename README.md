Author: Patrick Shinn 

Last Update 1/22/16 


------------------------------------------------------------------------------------------------------------------------
### General Description
WAN IP Checker Version 4.6 
Setup Version 2 

The purpose of the software is to check the current IP address of the network it is on and record it. In the event that
the address changes, the program will send an email out to inform the server owner of the change. If owncloud is run on
the server, the config file will automatically be updated to allow access from the new address.

------------------------------------------------------------------------------------------------------------------------
### Setup

This software was designed for use on a home server using owncloud. This software may still be used if you do not run an
owncloud installation. Follow the directions to successfully install and use WAN IP Checker 4.5 and the companion setup
software. It is advised that you make an email account specifically for your server such as myserver@example.com
This was built using a gmail email for the email server, but has been tested for use with yahoo accounts as well.
This software was also developed and tested in Linux based environment.  It has been developed in a way that it should
be cross platform, but has never been tested on windows.

1. Install
Both Setup.py and WAN_Checker.py should be in a folder called wan-tracker. Place thia folder where ever you want on your
system. It is advised that if you run Linux that you place the wan folder in /opt as this is the optional software
directory.

2. Make Executable
Make both Setup.py and WAN_Checker.py executable so that they may be run on your system.

3. Setup First Run
 Run Setup.py, if you are on Linux and put the wan folder in /opt, you will need to run it with root permission. You
 can do this by typing this command in the terminal:

* sudo /opt/wan/Setup.py 

You will be asked for your password, then the program will execute. It is recommended that your first run of the setup
software be done in easy mode. It will automatically configure all settings with minimal input from you. If you wish,
you can also run manual configuration, but this is not recommended unless you know what you are doing.


4. Securing Your Instillation
Now that everything is installed and working, you need to secure these files as they contain sensitive information such
as email password. To do this on a Linux system or a mac, open the terminal and cd into the wan directory.
Then use the following command:
sudo chown root:root *; sudo chmod 700 Setup.py WAN_Checker.py; sudo chmod 500 settings.txt status.txt

This will put all of the files capable of reading and writing to the settings file under the control of root, meaning no
other users can read the or change them. This also means that in order to run either Setup.py or WAN_Checker.py,
you have to run them using sudo.

5. Automation of WAN_Checker.py
This program was designed to be automated, this can be achieved using crontabs on Linux. To add do this, use the
command: 

* sudo crontabs -u root -e 

This will make a command that root executes, so the files can be run properly.
Pick nano or the editor of your choice. Scroll to the bottom of the page, then add the following:

* * * * * * python3 /opt/wan/WAN_Checker.py 2> /opt/wan/error.log

This will run the wan checker as root and record all errors to the wan directory. This is setup assuming that you used
/opt as the install directory. If you installed it else where, please rerun the crontab command and edit it to be:

* * * * * * * python3 path/to/WAN_Checker.py 2> /path/to/wan folder

------------------------------------------------------------------------------------------------------------------------
### Trouble Shooting

This script is not full proof, this was designed to run on a Linux server running Ubuntu. You may have to do further
reading to get it working. 

------------------------------------------------------------------------------------------------------------------------
### Contact

If you have anything to contribute to this software, please email me at shinn16@marshall.edu This software is open
source and is to be shared with all who wish to view it. Feel free to fork it and do with it as you need.
