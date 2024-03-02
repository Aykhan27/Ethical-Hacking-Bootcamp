import socket

def scan_ports(ip_address, start_port, end_port):
    print(f"[+] Scanning target {ip_address} from port {start_port} to port {end_port}...")
    for port in range(start_port, end_port + 1): 
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1) 
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                print(f"[+] Port {port} is open")
            sock.close()
        except KeyboardInterrupt:
            print("\n [-] Closing !!!")
            break
        except socket.error:
            print("[-] Couldn't connect to server")

if __name__ == "__main__":
    target_ip = input("[+] Enter target IP address: ")
    start_port = int(input("[+] Enter starting port: "))
    end_port = int(input("[+] Enter ending port: "))
    scan_ports(target_ip, start_port, end_port)