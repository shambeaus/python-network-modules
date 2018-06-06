import json
import os
from napalm.base import get_network_driver

device_ip = '192.168.1.76'
username = 'cisco'
password = os.getenv('ciscopass')


driver = get_network_driver('ios')
conn = driver(hostname='192.168.1.220', username=username,
             password=password)
conn.open()
info = conn.get_facts()
conn.close()

print(json.dumps(info))