from pexpect import pxssh
import os
import getpass

username = 'testuser'
password = os.getenv('pass')
device_ip = '192.168.1.76'
commands = ['dir', 'ls', 'ifconfig']


def pxssh_run_commands(username, password, device_ip, commands):
    output = ''
    try:
        ssh = pxssh.pxssh()
        ssh.login(device_ip, username, password)
    except pxssh.ExceptionPxssh as e:
        print('unable to connect')
        print(e)

    for command in commands:
        ssh.sendline(command)
        ssh.prompt()
        output += ssh.before

    ssh.logout()
    return output


result = pxssh_run_commands(username, password, device_ip, commands)

print(result)
