import socket
from concurrent.futures import ThreadPoolExecutor
from socket import gaierror

# Define target ports
ports = [21, 22, 80, 443, 445, 3306, 25, 5432]
# 21 = FTP / 22 = SSH / 80 = HTTP / 443, 445 = SMB / 3306 = MySQL / 25 = SMTP / 5432 = Postgres


def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.settimeout(0.1)  # Adjust the scan speed as needed
            code = client.connect_ex((target, port))
            if code == 0:
                print(f"Port {port} OPEN")
    except socket.error as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Scan interrupted.")
        exit()
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    target = input("Enter the target domain or IP address: ")
    try:
        ip_address = socket.gethostbyname(target)
    except gaierror:
        print("Invalid domain or IP address.")
        exit()

    print(f"Scanning target: {ip_address}")

    with ThreadPoolExecutor(max_workers=10) as executor:
        for port in ports:
            executor.submit(scan_port, ip_address, port)


if __name__ == "__main__":
    main()
