from pexpect import pxssh
import os
import getpass

username = 'cisco'
password = os.getenv('ciscopass')
device_ip = '192.168.1.76'

try:
    ssh = pxssh.pxssh()
    ssh.login(device_ip, username, password)
    ssh.sendline('ls')  # run a command
    ssh.prompt()  # match the prompt
    print(ssh.before)  # print everything before the prompt.
    ssh.sendline('ifconfig')
    ssh.prompt()
    print(s.before)
    ssh.logout()
except pxssh.ExceptionPxssh as e:
    print('unable to connect')
    print(e)
