import threading
from queue import Queue
import os
from netmiko import ConnectHandler, file_transfer

# device details

USER = 'cisco'
PASSWORD = os.getenv('ciscopass')
device_details = {'device_type': 'cisco_asa',
                  'username': USER,
                  'password': PASSWORD,
                  'verbose': False}

# File details

source_file = 'test.txt'
dest_file = 'codefile.bin'
file_system = 'disk0:'
direction = 'put'

device_ips = ['192.168.1.76', '192.168.1.79']


def code_upload(ip, device_details, output_q):
    output_dict = {}
    hostname = ip
    device_details.update({'ip': ip})
    connection = ConnectHandler(**device_details)
    print('starting file transfer to device: ' + ip)
    transfer_result = file_transfer(connection,
                                    source_file=source_file,
                                    dest_file=dest_file,
                                    file_system=file_system,
                                    direction=direction,
                                    overwrite_file=True)
    output_dict[hostname] = transfer_result
    output_q.put(output_dict)


if __name__ == "__main__":

    upload_result = {}
    output_q = Queue()

    for ip in device_ips:
        thread = threading.Thread(target=code_upload, args=(ip, device_details, output_q))
        thread.start()

    main_thread = threading.currentThread()
    for new_thread in threading.enumerate():
        if new_thread != main_thread:
            new_thread.join()

    while not output_q.empty():
        upload_result.update(output_q.get())

    for k, v in upload_result.items():
        print(k)
        for k1, v1 in v.items():
            if 'file_transferred' in k1:
                print('File transfer result : ' + str(v1))
            if 'file_verified' in k1:
                print('File verified : ' + str(v1))
        print('-------------')
