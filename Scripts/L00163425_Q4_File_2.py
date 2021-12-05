"""
# ---------------------------
# File           : L00163425_Q4_File_2.py
# Created        : 04-12-2021 21:28
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description
# Using Python code to determine which ports are open
# Where  port  22  is  shown  as  open  display  the  word
# “SSH” where port 80 is shown as open display the word “HTTP”.
# ---------------------------
"""
import socket  # socket module provides various objects, constants, functions including client and server programs.
import subprocess # subprocess module used to run new codes and applications by creating new processes.
import sys # The sys module provides information about constants, functions and methods of the Python interpreter.
from datetime import datetime # import the datetime module and display the current date
def port_scan():
    """
    Display the ports are open
    and also display the port 22 and port 80
    parameter:
    none
    return:
    return the open and close port and also with display words
    :return:
    """
    # Clear the screen  #use clear if running in  *nix
    subprocess.call("cls", shell=True)
    # Ask for input
    remoteServer = input("Enter a remote host to scan: ")
    remoteServerIP = socket.gethostbyname(remoteServer)
    # Print a nice banner with information on which host we are about to scan
    print("-" * 60)
    print("Please wait, scanning remote host {} for ports between [1, 80]".format(remoteServerIP))
    print("-" * 60)

 # Check what time the scan started
    t1 = datetime.now()
    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)
    # We also put in some error handling for catching errors
    try:
        # try 1, 1025 if you have time
        for port in range(1, 81): # check the port from 1 to 80
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                if port == 22:
                    print("SSH port {} is open".format(port))
                elif port == 80:
                    print("HTTP port {} is open".format(port))
                else:
                    print("port {} is open".format(port))
            else:
                if port == 22:
                    print("SSH port {} is closed".format(port))
                elif port == 80:
                    print("HTTP port {} is closed".format(port))
                else:
                    print("Port {} is closed".format(port))

            sock.close()
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()
    except socket.error:
        print("Couldn't connect to server")
        sys.exit()
    # Checking the time again
    t2 = datetime.now()
    # Calculates the difference of time, to see how long it took to run the script
    total = t2 - t1
    # Printing the information to screen
    print('Scanning Completed in: ', total)

if __name__ == "__main__":
    port_scan() # call the function port_scan

