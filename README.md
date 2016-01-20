WAN IP Checker Version 4.1
Setup Version 1.2
Author: Patrick Shinn
Last Update 1/16/16
------------------------------------------------------------------------------------------------------------------
General Description

The purpose of the software is to check the current IP address of the network it is on and record it. In the event
that the address changes, the program will send an email out to inform the server owner of the change. If owncloud
is run on the server, the config file will automatically be updated to allow access from the new address.
------------------------------------------------------------------------------------------------------------------
Setup

This software was designed for home cloud server using owncloud. This software may still be used if you do not run
an owncloud installation. Follow the directions to succesfullly install and use WAN IP Checker 4.3 and the companion
setup software. It is advised that you make an email account specifically for your server such as myserver@example.com.
This was built using a gmail email for the server.

1. Move both Setup.py and WAN_Checker.py into a folder called wan, then place that folder where ever you want on your
  system. It is advised that if you run linux that you place the wan folder in /opt as this is the optional software
  directory.

2. Make both of the .py files executable

3. Run Setup.py, if you are on linux and put the wan folder in /opt, you will need to run it with root permission.
   You can do this by typing this command in the termainl: sudo /opt/wan/Setup.py 
   You will be asked for your password, then the program will execute.
   
   Here are some helpful settings for email configuration:
   Gmail: 
   server address = smtp.gmail.com
   port = 587
   Yahoo:
   server address = smtp.yahoo.com
   port = 587
   
   Other emial providers have not been tested.
   
4. If this is your first time running the Setup.py, you need to select option 1, configure. You will then be asked 
   a series of questions about your severver and email setup. Make sure you use absolute paths to files and the 
   proper email settings, otherwise the program will fail to run. For your first install, your email subject should
   read WAN Test or something similar. You can go back and change this by running Setup.py again and selecting option
   2, edit.
   
5. Now that everything is installed and working, you need to secure these files as they contain senstive information
   such as email password. To do this on a linux system or a mac, open the terminal and cd into the wan directory.
   Then use the following command: sudo chown root:root *; sudo chmod 700 Setup.py WAN_Checker.py; sudo chmod 500 settings.txt
   This will put all of the files capable of reading and writing to the settings file under the control of root, 
   meaning no other users can read the or change them. This also means that in order to run either Setup.py or WAN_Checker.py,
   you have to run them using sudo.
   
6. This program was designed to be automated, this can be achieved using crontabs on linux. To add do this, use the
   command: sudo crontabs -u root -e 
   This will make a command that root executes, so the files can be run properly.
   Pick nano. Scroll to the bottom of the page, then add the following:
   * * * * * python3 /opt/wan/WAN_Checker.py 2> /opt/wan/error.log
   This will run the wan checker as root and record all erros to the wan directory. This is setup assuming that you
   used /opt as the install directory. If you installed it else where, please rerun the crontab command and 
   edit it to be: * * * * * python3 path/to/WAN_Checker.py 2> /path/to/wan folder
--------------------------------------------------------------------------------------------------------------------
 Trouble Shooting
 
 This script is not full proof, this was designed to run on a linux server running ubuntu. You may have to do further
 reading to get it working. 
--------------------------------------------------------------------------------------------------------------------
Contact

If you have anything to contribute to this software, please email me at patrick_shinn@yahoo.com. This software is opensource
and is to be shared with all who wish to view it.
