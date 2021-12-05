"""
# ---------------------------
# File           : L00163425_Q5_File_2.py.py
# Created        : 05-12-2021 12:23
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description
# Install curl,Create a directory structure Labs with subfolders lab1 and lab2
# From your home directory find out when files were last accessed.
# ---------------------------
"""
import time
import re
import paramiko # to connection the remote machine


def ssh_connection(ip, username, password):
    """Function to open SSH connection to the device
       parameter:
       passing the arguments ip address, username and password
       return:
       establish the connection in remote machine with directories contain 2 subfolders
       and also access time
    """

    try:
        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username,
                        password=password)
        connection = session.invoke_shell()
        session.exec_command("sudo -S apt-get install curl")
        connection.send("mkdir labs\n")  # unix command to make directory
        connection.send("mkdir labs/lab1\n") # unix command to create subfolders in folders
        connection.send("mkdir labs/lab2\n")
        time.sleep(1)
        vm_output = connection.recv(65535)
        print(vm_output)
        if re.search(b"% Invalid input", vm_output):
            print("There was an error on vm {}".format(ip))
        else:
            print("Commands successfully executed on {}".format(ip))
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")


if __name__ == '__main__':
    ssh_connection("192.168.189.129", "l00163425", "admin") # calling the function ssh connection from the main