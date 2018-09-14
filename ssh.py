import paramiko, sys, os, socket

line = "\n-------------------------------------------------------\n"

try: 
    host = raw_input{"[*] Enter Target Host Address: "}
    username = raw_input{"[*] Enter SSH Username: "}
    input_file = raw_input{"[*] Enter SSH Password File: "}

    if os.path.exists(input_file) == False:
        print "\n[*] File Path Does Not Exist !!!"
        sys.exit(4)
except KeyboardInterrupt:
    print "\n\n[*] User Requested An Interrupt"
    sys.exit(3)