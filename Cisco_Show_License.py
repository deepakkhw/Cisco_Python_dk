import paramiko
import time
import datetime
import re
import sys
import getpass
import time
from datetime import date
from datetime import datetime
import os
import socket


def get_filename_datetime():
    # Use current date & time to get a text file name.
        return str(datetime.now().strftime('%Y_%m_%d %H_%M_%S'))

# Get full path for writing.
fname = get_filename_datetime()

#Input for Python3 and raw_input for Python2
#user = input("Enter your M-account: ")
user = raw_input('Enter your M-account: ')
password = getpass.getpass("Enter your M-account Password: ")

ssh = paramiko.SSHClient()

ips = [i.strip() for i in open("switchlist.txt")] # creates a list from input file

for HOST in ips:
    try:
        #date_time = datetime.datetime.now().strftime("%Y-%m-%d")
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(HOST, port=22, username=user, password=password, look_for_keys=False, timeout=8, banner_timeout=5)
        connection = ssh.invoke_shell()
        connection.send("terminal length 0\n")
        connection.send("show version\n")
        time.sleep(10)
        connection.send("show license right-to-use\n")
        connection.send("sho license feature-version\n")
        connection.send("sho license right-to-use\n")
        connection.send("sho license file\n")
        connection.send("sho license summary\n")
        connection.send("sho license  status\n")
        connection.send("sho license reservation\n")
        time.sleep(2)
        file_output = connection.recv(99999999).decode(encoding='utf-8')
        hostname = (re.search('(.+)#', file_output)).group().strip('#')
        print(file_output)
        #outFile = open(hostname + "_" + HOST + ".txt", "w")
        outFile = open('Switches_License_Details.txt', 'a+')
        outFile.writelines(file_output)
        outFile.close()
        ssh.close()
        print("*" * 20 + " " + "%s is done" % hostname + " " + "*" * 20)

    except paramiko.AuthenticationException:
        print("X" * 20 + " " + HOST + ' === Bad credentials ' + "X" * 20)
    except paramiko.SSHException:
        print("X" * 20 + " " + HOST + ' === Issues with ssh service ' + "X" * 20)
    except socket.error:
        print("X" * 20 + " " + HOST + ' === Device unreachable ' + "X" * 20)
