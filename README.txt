WAN IP Checker Version: 4.6
Setup Version: 2
Install Script Version: 1
Update Script Version: 1.1
Author: Patrick Shinn
Last Update 1/22/16

------------------------------------------------------------------------------------------------------------------------
### General Description

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
Please ensure that you have Python 3 installed on your system before running this software.
Clone the WAN_Tracker repository to the machine you wish to install on, the cd into the WAN-Tracker folder and make
install.sh executable. Then run it, following the on screen prompts.

2. Update
To update this software, you must have git installed on your machine. To update, cd into the WAN-Tracker folder and make
update.sh executable. Then run it, following the on screen prompts.

3. Uninstall
Comming soon.

------------------------------------------------------------------------------------------------------------------------
### Trouble Shooting

This script is not full proof, this was designed to run on a Linux server running Ubuntu. You may have to do further
reading to get it working.

------------------------------------------------------------------------------------------------------------------------
### Contact

If you have anything to contribute to this software, please email me at shinn16@marshall.edu This software is open
source and is to be shared with all who wish to view it. Feel free to fork it and do with it as you need.