import  paramiko, sys, os, socket
global host, username, line, input_file

line = "\n-------------------------------------------------------\n"

#collect program information
try: 
    #hold target address
    #hold ssh username to be bruteforced
    #hold file path string
    host = raw_input("[*] Enter Target Host Address: ")
    username = raw_input("[*] Enter SSH Username: ")
    input_file = raw_input("[*] Enter SSH Password File: ")

    #check if file exists. If it doesn't, print as follows.
    if os.path.exists(input_file) == False:
        print "\n[*] File Path Does Not Exist !!!"
        sys.exit(4)
except KeyboardInterrupt:
    print "\n\n[*] User Requested An Interrupt"
    sys.exit(3)

