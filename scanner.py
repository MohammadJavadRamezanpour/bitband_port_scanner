import socket, sys
from colorama import init, Fore, Back, Style

init(autoreset=True)

if len(sys.argv) != 2:
    print("USAGE: python3 scanner.py <url-ip>")
else:
    ip = sys.argv[1]
    for port in range(65536):
        print(f"testing port {Fore.RED}{port}", end="\r")
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
                connection.settimeout(0.5)
                connection.connect((ip, port))
                print(f"{Fore.GREEN}port {port} is open")
        except:
            pass
