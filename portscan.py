import socket

# 21 = FTP / 22 = SSH / 80 = HTTP / 443, 445 = SMB / 3306 = MySQL / 25 = SMTP / 5432 = Postgres
ports = [21, 22, 80, 443, 445, 3306, 25, 5432]

target = input("Enter the target domain (ex: example.com): ")

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)  # change the scan speed
    code = client.connect_ex((target, port))  # defining the domain that will be scanned

    if code == 0:  # 0 = connection established
        print(port, "OPEN")
