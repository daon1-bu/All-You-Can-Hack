import socket
import ipaddress

print("RUNNING...")
COMMON_PORT={
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "Pop3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP",
}

def is_open(host: str, port: int, timeout: float =0.8) -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        return s.connect_ex((host, port)) ==0
    finally:
        s.close()


def main():
    print("Simple Port Scanner\n")

   

    host = input("Target (IP or domain): ").strip()

    try:
        ipaddress.ip_address(host)
    except ValueError:
        print("Invalid IP address format.")
        return
    
    print(f"\nScanning {host}...\n")
    
    

    found = False


    
    for port, name in COMMON_PORT.items():
        if is_open(host, port):
            found = True
            print(f"[OPEN] {port} - {name}")

    if not found:
        print("No common port open.")
    
    input("\nScan complete. Press Enter to exit...")

if __name__=="__main__":
    main()