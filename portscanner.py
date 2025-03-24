#SIMPLE PORT SCANNER PROJECT USINNG SOCKET 
#AUTHOR:A.ARUVASAGA CHITHAN
#REQUIREMENTS ARE IN requirement.txt
import argparse
import socket
import sys
from pyfiglet import Figlet
from colorama import init, Fore, Style

def figlet(): # Function for printing title 
    init(autoreset=True) # Initialize resetting 
    HEADING = Style.BRIGHT
    print(f"{HEADING}{Fore.RED}AUTHOR: A.ARUVASAGA CHITHAN")
    print(f"{HEADING}{Fore.BLUE}SIMPLE TCP PORT SCANNER")
    figlet = Figlet(font='slant') # Font style
    ascii_art = figlet.renderText("PORT SCANNER") # Convert text to ASCII art and store it in ascii_art variable
    print(f"{Fore.RED}{ascii_art}")

figlet()

def scan_port(ip, port, show_closed): # Function used to scan port
    try:
        HEADING = Style.BRIGHT#For colored  and bold text
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Specifying socket family for IPv4
        s.settimeout(1) # Setting time in seconds
        result = s.connect_ex((ip, port)) # connect_ex function returns 0 or 1; when the connection is successful, it returns 0; if it fails, it returns 1
        if result == 0: # If the connection succeeds, print open ports
            print(f"{HEADING}Port {port} is {HEADING}{Fore.GREEN}open")
            return True # Return True for open port
        elif show_closed: # Print closed ports only if show_closed is True
            print(f"{HEADING}Port {port} is {HEADING}{Fore.RED}closed")
        return False # Return False for closed port
        s.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        return False
    print(ip)
def parse_port(port_str): # Function for parsing the command line inputs
    try:
        if '-' in port_str:
            start_port, end_port = map(int, port_str.split('-')) # Split the range and convert into integers
            return range(start_port, end_port + 1)
        else:
            return [int(port_str)]
    except ValueError:
        print(f"Error: Invalid port format '{port_str}'. Use a single port (e.g., 80) or a range of ports (e.g., 20-24)")
        sys.exit(1) # Exit function if any error occurred

def main(): # Main function
    HEADING = Style.BRIGHT
    parser = argparse.ArgumentParser(description="Simple TCP port scanner") # Give a small description
    parser.add_argument('-H', '--host', required=True, help="Target IP address (e.g., 192.168.1.1)") # Add a command line argument for host
    parser.add_argument('-p', '--ports', required=True, help="Target port or a port range (e.g., 20 or 20-24)") # Add a command line argument for port
    args = parser.parse_args() # Parsing arguments
    try:
        socket.inet_aton(args.host) # Validating IP address 
    except socket.error:
        print(f"Error: Invalid IP address '{args.host}'")
        sys.exit(1) # Exit function returning 1

    port_range = parse_port(args.ports) # Calling parse_port function and passing args.ports as an argument
    show_closed = len(port_range) == 1 # Determine if we should show closed ports (only for single port)

    open_count = 0
    closed_count = 0
    total_ports=len(port_range)

    for port in port_range:
        if scan_port(args.host, port, show_closed): # Calling scan_port function and passing host, port, and show_closed as arguments
            open_count += 1
        else:
            closed_count += 1
    

    # Print the summary
    print(f"\n{Fore.GREEN}Scan completed!")
    print(f"{Fore.GREEN}TOtally {total_ports} ports are scanned successfully")
    print(f"{HEADING}{open_count} open ports")
    print(f"{HEADING}{closed_count} closed ports")

if __name__ == "__main__":
    main()

