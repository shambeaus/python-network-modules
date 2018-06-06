from netmiko import ConnectHandler
import os

ciscoasa = {
    'device_type': 'cisco_asa',
    'ip': '192.168.1.76',
    'username': 'cisco',
    'password': os.getenv('ciscopass'),
}

conn = ConnectHandler(**ciscoasa)

config_commands = ['pager 0', 'logging permit-hostdown']

output = conn.send_config_set(config_commands)
wr = conn.save_config()
conn.disconnect()


print(output)
print(wr)