import pexpect
import os
import sys

username = 'cisco'
password = os.getenv('ciscopass')
device_ip = '192.168.1.76'
debug = False

ssh_newkey = "Are you sure you want to continue connecting"

ssh_asa = 'ssh {}@{}'.format(username, device_ip)

child = pexpect.spawnu(ssh_asa)

if debug:
    child.logfile = sys.stdout

response = child.expect([ssh_newkey, 'assword'])

if response == 0:
    print("saw ssh newkey")
    child.sendline("yes")
    child.expect('assword')
    child.sendline(password)
elif response == 1:
    print('sending password')
    child.sendline(password)

child.expect('#')
child.sendline('show ip')

child.expect('#')
sh_ip = child.before

child.sendline('show route')
child.expect('#')
sh_route = child.before

print('=============================')
print(sh_ip)
print('=============================')
print(sh_route)