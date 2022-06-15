#!/bin/python3
import sys
import socket
from datetime import datetime


# Defining target
if len(sys.argv) < 2:
    print("Provide an ip adress to scan.")

else:
    target = sys.argv[1]
    if len(sys.argv) < 3:
        print("Syntax: ./port_scanner.py <ip> <Port start> <Port end>\n./port_scanner.py 127.0.0.1 1 65535")
        p_start, p_end = 1, 65535
        print(p_start, p_end)

    else:
        p_start = int(sys.argv[2])
        p_end = int(sys.argv[3])
        try:
            print("In try")
            for port in range(p_start, p_end):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                res = s.connect_ex((target, port))
                if res == 0:
                    print(f"Port # {port} is open.")
                s.close
        except KeyboardInterrupt:
            print("Keyboard interrupt.\nExiting program")
            sys.exit()
        except socket.gaierror:
            print("Hostname could not be resolved.")
            sys.exit()
        except socket.error:
            print("Could not connect to server.")
            sys.exit()
