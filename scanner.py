import socket, sys
from colorama import init, Fore

# initialize the colorama module
init(autoreset=True)

# if sys.argv has less or more than 2 items, it means 
# user doesnt know how to use the script, so we show him
# how to use it, otherwise we do the business
if len(sys.argv) != 2:
    print("USAGE: python3 scanner.py <url-ip>")
else:
    # extract the ip from argument variable, it lives at index 1
    # index 0 is the name of the module, here 'scanner.py
    ip = sys.argv[1]

    # now go from 0 to 65535, thats the possible range for port number
    # try to connect with ip user provided and the port you have in each iteration
    # if you connected, show us the port number, if not it will raise an error
    # we will handle the error in the except block, we will simply pass it :|
    for port in range(65536):
        print(f"testing port {Fore.RED}{port}", end="\r")
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
                connection.settimeout(1) # this is optional, but you dont want to wait for ever rigth?
                connection.connect((ip, port))
                print(f"{Fore.GREEN}port {port} is open")
        except:
            pass
