from netmiko import ConnectHandler
import os

ciscoasa = {
    'device_type': 'cisco_asa',
    'ip': '192.168.1.76',
    'username': 'cisco',
    'password': os.getenv('ciscopass'),
}

# create connection object
conn = ConnectHandler(**ciscoasa)

# issue show commands to device
run = conn.send_command('show run')
ip = conn.send_command('show ip')

show_multiple = ['show arp', 'show route']

arp = [conn.send_command(command) for command in show_multiple]

print(run)
print('--------')
print(ip)
print('--------')
print(arp[0])
print(arp[1])

conn.disconnect()

