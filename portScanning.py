# This Script file will scan for Open Ports of hosts
# In a given IP Range 

import sys
import socket


def port_scan(target_host, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Set a timeout for the connection attempt
            sock.settimeout(1)

            # Attempt to connect to the target host and port
            result = sock.connect_ex((target_host, port))

            if result == 0:
                # If the connection is successful, the port is open
                open_ports.append(port)

            # Close the socket
            sock.close()

        except socket.error:
            # If an exception occurs, assume the port is closed
            pass

    return open_ports


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python port_scanner.py <target_host> <start_port> <end_port>")
        sys.exit(1)

    target_host = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    open_ports = port_scan(target_host, start_port, end_port)

    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(port)
    else:
        print("No open ports found.")
