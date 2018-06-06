from netmiko import ConnectHandler, file_transfer
import os

def main():
    print('Interactive script to scp files to network devices with netmiko')
    print('--------')
    print('Chose direction of file transfer')
    print('1. From LOCAL to REMOTE')
    print('2. From REMOTE to LOCAL')
    transfer_direction = input()

    if transfer_direction == '1':
        direction = 'put'
        source_file = input('Source file name : ')
        dest_file = input('Destination file name : ')
        file_system = 'disk0:'

        ciscoasa = {
            'device_type': 'cisco_asa',
            'ip': '192.168.1.76',
            'username': 'cisco',
            'password': os.getenv('ciscopass'),
        }

        ssh_conn = ConnectHandler(**ciscoasa)
        transfer_dict = file_transfer(ssh_conn,
                                      source_file=source_file,
                                      dest_file=dest_file,
                                      file_system=file_system,
                                      direction=direction,
                                      overwrite_file=True)

        print(transfer_dict)

    elif transfer_direction == '2':
        direction = 'get'
        dest_file = input('Destination file name on remote device : ')
        source_file = input('Source file : ')
        file_system = 'disk0:'

        ciscoasa = {
            'device_type': 'cisco_asa',
            'ip': '192.168.1.76',
            'username': 'cisco',
            'password': os.getenv('ciscopass'),
        }

        ssh_conn = ConnectHandler(**ciscoasa)
        transfer_dict = file_transfer(ssh_conn,
                                      source_file=source_file,
                                      dest_file=dest_file,
                                      file_system=file_system,
                                      direction=direction,
                                      overwrite_file=True)

        print(transfer_dict)


if __name__ == "__main__":
    main()