import netmiko
from netmiko import ConnectHandler

# Device Information
device_info = {
    'device_type': 'cisco_ios_telnet', 
    'host': '10.255.10.130', 
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass',
    'port': 23 
}

# Config
device_config = [
    'int loopback 1',
    'ip add 1.1.1.1 255.255.255.255',
    'end'
]

# Connect to Device
access_cli = ConnectHandler(**device_info)
access_cli.enable()
output = access_cli.send_config_set(device_config)
siib = access_cli.send_command('show ip int br')
access_cli.disconnect()

print(output)
print(siib)
