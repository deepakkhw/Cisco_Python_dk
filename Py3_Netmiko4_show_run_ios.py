import sys
from netmiko import ConnLogOnly
import getpass

Hostname = input("Please enter Switch/Router IP address: ")
username = input("Please enter username: ")
password = getpass.getpass("Please enter Password: ")

Cisco_ios = {
    "device_type": "cisco_ios",
    "ip": Hostname,
    "username": username,
    "password": password,
    'global_delay_factor': 4
    }
login = ConnLogOnly(**Cisco_ios)
if login is None:
    # Errors will be logged in 'netmiko.log'
    sys.exit("Logging in failed")
show_otuput = login.send_command("show run")

file = open(Hostname + '.txt', 'w')
file.write(show_otuput)
file.close()
print(show_otuput)
login.disconnect()