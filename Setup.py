#! /usr/bin/python3
"""
@author Patrick Shinn
@version 2
Last Updated: 1/17/16
This is the setting setup for WAN_Checker.py, run this before running WAN_Checker.py
This program will ask a series of ten questions to the user to get the proper settings.
"""
import os
done = False  # Boolean for loops  # Settings file to be written to
oldSettings = False  # initial value for old settings test
settingsList = []  # Stores setting values to be written
previousSettings = ''  # will be used to check for old settings
settingWrite = False  # checks to see if the setting were written before closing the program
mode = ''  # first run mode question storage
welcomeText = 'This program will configure the settings for WAN_Checker.py, to ensure that \n' \
              'the settings are correct, please be sure to enter the correct information. Spelling counts.\n' \
              'If you are having issues or have questions, please refer to the README.txt. \n' \
              'Windows support is in beta at this time. \n'
pwd = os.getcwd()  # gets current
pwd = pwd.strip('"\'\n\t')

# empty variables for storing values to be written to settingsList
######################################################################################################################
phpConfig = ''
logFile = ''
oldWan = ''
recipient = ''
sender = ''
password = ''
subject = ''
serverAddress = ''
serverPort = ''
operatingSystem = ''
######################################################################################################################

# Begin program

# checks for an old settings file to read
try:
    previousSettings = open('settings.txt', 'r')
    oldSettings = True  # indicates that a settings file exists
except FileNotFoundError:
    pass

if oldSettings is True:  # if old settings are found, read and imported
    for setting in previousSettings:
        setting = setting.strip()
        settingsList.append(setting)

print(welcomeText)
if oldSettings is False:  # lets the user know that no previous settings were found
    print("No previous settings were found, please select a configuration mode.\n")
    print("1. Manual (Not recommended for novice programmers).\n"
          "2. Easy Setup (recommended). \n")
    mode = input("Enter your selection number: ")
else:  # If a settings file is found, setup is opened in manual config mode.
    print("A settings file was found, you can either edit the file or start fresh by deleting settings.txt. \n")
    mode = '1'

while not done:
    if mode == '2':
        while mode == '2':  # while in easy mode, this code executes
            # User will answer the following questions, and the script will try to automate as much as it can.
            q1 = input("Does your server run owncloud? yes/no: ")
            if q1.lower() == 'no':
                phpConfig = 'none'
            else:
                q1 = input("What is the absolute path to your config.php file?: ")
                phpConfig = q1
            q2 = input("What email would you like address changes to be send to?: ")
            q3 = input("What email would you like to send the alerts from?: ")
            q4 = input("What is the sender email's password?: ")
            q7 = input("What would you like the email's subject to be?: ")
            q5 = input("Is the sender email a gmail or a yahoo account? If neither, say neither: ")
            emailConfirm = False
            while not emailConfirm:  # preset email server settings.
                if q5.lower() == 'gmail':
                    serverAddress = 'smtp.gmail.com'
                    serverPort = '587'
                    emailConfirm = True
                elif q5.lower() == 'yahoo':
                    serverAddress = 'smtp.mail.yahoo.com'
                    serverPort = '587'
                    emailConfirm = True
                elif q5.lower() == 'neither':
                    mode = '1'
                    print("You will need to manually configure your settings, please select option 1"
                          " to configure settings.")
                    break
                else:
                    print('"' + q5 + '"' + ' was not an option, please try again.')
                    q5 = input("Is the sender email a gmail or a yahoo account? If neither, say neither: ")
            if mode == '1':
                break
            q6 = input("What is your operating system? Windows, OSX, or Linux?: ")
            if q6.lower() == 'windows':  # Windows config
                oldWan = pwd + '\\wan.txt'
                logFile = pwd = '\\log.txt'
            else:  # Linux and OSX config
                oldWan = pwd + '/wan.txt'
                logFile = pwd + '/log.txt'

            recipient = q2
            sender = q3
            password = q4
            operatingSystem = q6
            subject = q7
            #  Appends settings to settings list for writing
            settingsList.append(phpConfig)
            settingsList.append(logFile)
            settingsList.append(oldWan)
            settingsList.append(recipient)
            settingsList.append(sender)
            settingsList.append(password)
            settingsList.append(subject)
            settingsList.append(serverAddress)
            settingsList.append(serverPort)
            settingsList.append(operatingSystem)
            mode = '1'

    elif mode == '1':  # manual config mode
        # Options menu
        print("What would you like to do? \n"
              "1. Configure Settings\n"
              "2. Edit Settings\n"
              "3. Check settings\n"
              "4. Save settings\n"
              "5. Finish\n")
        userChoice = input("Enter a number option: ")

        # Configure settings
        if userChoice == '1':
            settingWrite = False
            settingsList = []
            phpConfig = input("What is the path to your owncloud config.php file? If you do not"
                              "have one, put 'none': ")
            logFile = input("What is the path to your desired log file location?: ")
            oldWan = input("What is the path to your desired wan storage? This "
                           "should be in the same folder as WAN_Checker.py: ")
            recipient = input("What email should the email be sent to?: ")
            sender = input("What email will be sending the message?: ")
            password = input("What is the password for the sending email?: ")
            subject = input("What should the subject of the email be?: ")
            serverAddress = input("What is you email providers server address?: ")
            serverPort = input("What port number does your email sever use?: ")
            operatingSystem = input("What is your operating system? Windows, Linux, or OSX(apple)?: ")

            # Appending settings to setting list for temporary storage
            settingsList.clear()  # clears all settings for clean write
            settingsList.append(phpConfig)
            settingsList.append(logFile)
            settingsList.append(oldWan)
            settingsList.append(recipient)
            settingsList.append(sender)
            settingsList.append(password)
            settingsList.append(subject)
            settingsList.append(serverAddress)
            settingsList.append(serverPort)
            settingsList.append(operatingSystem)
            print('\n' * 5)

        # edit settings
        elif userChoice == '2':
            settingWrite = False
            apply = False
            while not apply:
                print('Which setting would you like to change?\n'
                      '1. php.config file\n'
                      '2. log file\n'
                      '3. wan file\n'
                      '4. recipient email\n'
                      '5. sender email\n'
                      '6. sender password\n'
                      '7. subject\n'
                      '8. email server address\n'
                      '9. email server port\n'
                      '10. operating system\n')
                userChange = input("Please select a number option or type 'done' to exit: ")
                if userChange == '1':
                    userRewrite = input("What should the new php.config location be?: ")
                    settingsList.pop(0)
                    settingsList.insert(0, userRewrite)
                elif userChange == '2':
                    userRewrite = input("What should the new log location be?: ")
                    settingsList.pop(1)
                    settingsList.insert(1, userRewrite)
                elif userChange == '3':
                    userRewrite = input("What should the new wan location be?: ")
                    settingsList.pop(2)
                    settingsList.insert(2, userRewrite)
                elif userChange == '4':
                    userRewrite = input("What should the new recipient email be?: ")
                    settingsList.pop(3)
                    settingsList.insert(3, userRewrite)
                elif userChange == '5':
                    userRewrite = input("What should the new sender email be?: ")
                    settingsList.pop(4)
                    settingsList.insert(4, userRewrite)
                elif userChange == '6':
                    userRewrite = input("What should the new sender password be?: ")
                    settingsList.pop(5)
                    settingsList.insert(5, userRewrite)
                elif userChange == '7':
                    userRewrite = input("What should the new subject be?: ")
                    settingsList.pop(6)
                    settingsList.insert(6, userRewrite)
                elif userChange == '8':
                    userRewrite = input("What should the new email server address be?: ")
                    settingsList.pop(7)
                    settingsList.insert(7, userRewrite)
                elif userChange == '9':
                    userRewrite = input("What should the new server port be?: ")
                    settingsList.pop(8)
                    settingsList.insert(8, userRewrite)
                elif userChange == '10':
                    userRewrite = input("What should the new operating system be?: ")
                    settingsList.pop(9)
                    settingsList.insert(9, userRewrite)
                elif userChange.lower() == 'done':
                    break
                else:
                    print("'" + userChange + "'" + ' is not an option, please try again.')

        # Check settings
        elif userChoice == '3':
            print('The following will be written:' + '\n')
            print('The php file location is: ' + settingsList[0])
            print('The log file location is: ' + settingsList[1])
            print('The old wan file location is: ' + settingsList[2])
            print('The recipient email is: ' + settingsList[3])
            print('The sender email is: ' + settingsList[4])
            print('The sender password is: ' + settingsList[5])
            print('The email email subject is: ' + settingsList[6])
            print('The email server address is: ' + settingsList[7])
            print('The email server port is: ' + str(settingsList[8]))
            print('The operating system is: ' + settingsList[9])
            print('\n' * 2)

        # Write settings
        elif userChoice == '4':
            setting = open('settings.txt', 'w')  # Settings file to be written to
            for item in settingsList:
                setting.write(item + '\n')
            print('Settings written. \n')
            settingWrite = True
            setting.close()

        # End program
        elif userChoice == '5':
            if settingWrite is True:  # if the settings were written, do this
                print("Your settings have been saved.")
                # This section generates the log and wan storage files.
                if oldSettings is False:
                    log = open(logFile, 'w')
                    wan = open(oldWan, 'w')
                    wan.close()
                    log.close()
                done = True
            else:  # else tell the user that no settings were saved
                print("Your settings were never saved, to save your settings please write them before closing the "
                      "program.")
                retry = input("Would you like to go back and save your settings? yes/no: ")
                if retry.lower() == 'yes':
                    continue
                else:
                    done = True
