# Parallel Port Scanner

This Python script performs a parallel port scan on a specified domain name or IP address. It checks a predefined list of common ports to determine if they are open or closed. The script utilizes multithreading to improve scanning efficiency by scanning multiple ports concurrently.

## Features

1. **Efficient Port Scanning:** The script efficiently scans for open ports on the target machine using a predefined list of common ports.

2. **Parallel Execution:** Leveraging multithreading with ThreadPoolExecutor, the script scans multiple ports simultaneously, reducing scan time.

3. **Error Handling:** Robust error handling ensures the script gracefully handles network errors and interruptions, providing a smoother scanning experience.

4. **Input Validation:** Validates user input to ensure it is a valid domain name or IP address, enhancing script reliability.

## Usage

1. Run the script and input the target domain name or IP address when prompted.
2. The script will perform a parallel port scan on the target, displaying open ports as they are discovered.

## Requirements

- Python 3.x
- No additional libraries required.

## Example

```bash
$ python3 port_scanner.py
Enter the target domain or IP address: example.com
Scanning target: 93.184.216.34
Port 80 OPEN
Port 443 OPEN
