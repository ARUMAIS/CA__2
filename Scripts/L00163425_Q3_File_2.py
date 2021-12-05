"""
# ---------------------------
# File           : L00163425_Q3_File_2.py
# Created        : 22-11-2021 12:32
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description
# establish connection in VM using a python code using the ssh port
# ---------------------------
"""
import paramiko  # import paramiko module to connect the remote machine
import time  # import time module to calculate access time and conversion
import re  # import re module to use regular expressions


# Open SSH connection to the device
def open_ssh_connection(ip, username, password):
    """
    Establish a connection in VM using SSH service
    show the directory contents
    parameter:
    passing aruguments ip address,username and password in the method
    return:
    list of content inside the directories
    """
    try:

        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username,
                        password=password)
        connection = session.invoke_shell()
        connection.send("ls > dir_contents.txt\n")  # unix command to list directory contents and save to file
        time.sleep(1)

        vm_output = connection.recv(65535)
        if re.search(b"% Invalid input", vm_output):
            print("There was an error on vm {}".format(ip))
        else:
            print("Commands successfully executed on {}".format(ip))
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")

if __name__ =="__main__":

 open_ssh_connection("192.168.189.129", "l00163425", "admin")  # call the function open ssh connection & ip address of my VM, adjust to suit
