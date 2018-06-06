
import threading
from queue import Queue
from netmiko import ConnectHandler

USER = 'cisco'
PASSWORD = os.getenv('ciscopass')


device_ips = ['192.168.1.76', '192.168.1.76']


def ssh_session(ip, output_q):
    output_dict = {}
    hostname = ip
    device_details = {'device_type': 'cisco_asa', 'ip': ip, 'username': USER, 'password': PASSWORD, 'verbose': False, }
    ssh_session = ConnectHandler(**device_details)
    output = ssh_session.send_command("show version")
    output_dict[hostname] = output
    output_q.put(output_dict)


if __name__ == "__main__":

    output_q = Queue()

    for ip in device_ips:
        thread = threading.Thread(target=ssh_session, args=(ip, output_q))
        thread.start()

    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            some_thread.join()


    while not output_q.empty():
        my_dict = output_q.get()
        for k, v in my_dict.items():
            print(k)
            print(v)