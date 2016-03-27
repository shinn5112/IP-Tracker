Author: Patrick Shinn
Last Update: 3/27/16
Home Server WAN-Tracker Package V 1.0
------------------------------------------------------------------------------------------------------------------------
### Contents
* WAN IP Checker Version: 4.8
* Setup Version: 2.0
* Install Script Version: 1.0
* Update Script Version: 1.1
* Uninstall Script Version: 1.0

------------------------------------------------------------------------------------------------------------------------
### General Description

The purpose of the software is to check the current IP address of the network it is on and record it. In the event that
the address changes, the program will send an email out to inform the server owner of the change. If owncloud is run on
the server, the config file will automatically be updated to allow access from the new address.  In order to run this
software, the system will need at least python 3.4 installed.  You will also need to install git on the system to ensure
that the scripts run properly.  WAN-Tracker was designed in a way that if you have python 3 and git installed, you
should need no additional packages for it to run properly.

------------------------------------------------------------------------------------------------------------------------
### Setup

This software was designed for use on a home server using owncloud. This software may still be used if you do not run an
owncloud installation. Follow the directions to successfully install and use WAN-Tracker.
It is advised that you make an email account specifically for your server such as myserver@example.com
This was built using a gmail email for the email server, but has been tested for use with yahoo accounts as well.
This software was developed and tested in a Linux environment.  It has been developed in a way that it should
work on OSX as well, but has never been tested.  This software comes with absolutely no warranty.

1. ####Install
    Please ensure that you have Python 3 and git installed on your system before running this software.
git clone the WAN_Tracker repository to the machine you wish to install on, the cd into the WAN-Tracker folder and make
install.sh executable. Then run it, following the on screen prompts.

2. ####Update
    To update this software, you must have git installed on your machine. To update, cd into the WAN-Tracker folder and make
update.sh executable. Then run it, following the on screen prompts.

3. ####Uninstall
    To remove WAN-Tracker, cd into the WAN-Tracker folder and make uninstall.sh executable. Then run uninstall and follow
the on screen prompts. You may wish to make a copy of root's crontab file before hand as this program will wipe it.
Typically root has no crontab processes, so you should be safe if you don't.

------------------------------------------------------------------------------------------------------------------------
### Trouble Shooting

This software is not full proof, this was designed to run on a Linux server running Ubuntu. You may have to do further
reading to get it working.

------------------------------------------------------------------------------------------------------------------------
### Contact

If you have anything to contribute to this software, please email me at shinn16@marshall.edu This software is open
source and is to be shared with all who wish to view it. Feel free to fork it and do with it as you need.