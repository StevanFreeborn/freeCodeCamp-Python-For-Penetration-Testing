import nmap

scanner = nmap.PortScanner()

print('Welcome, this is a simple nmap automation tool')

ip_addr = input('Please enter the IP address you want to scan: ')
print(f'The IP you entered is: {ip_addr}')

type(ip_addr)

resp = input('Please enter the type of scan you want to run: \n1) SYN ACK Scan\n2) UDP Scan\n3) Comprehensive Scan\n')
print(f'You have selected option: {resp}')

if resp == '1':
    print(f'Nmap Version: {scanner.nmap_version()}')
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print(f'Ip Status: {scanner[ip_addr].state()}')
    print(scanner[ip_addr].all_protocols())
    print(f'Open Ports: {scanner[ip_addr]["tcp"].keys()}')
elif resp == '2':
    print(f'Nmap Version: {scanner.nmap_version()}')
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print(f'Ip Status: {scanner[ip_addr].state()}')
    print(scanner[ip_addr].all_protocols())
    print(f'Open Ports: {scanner[ip_addr]["udp"].keys()}')
elif resp == '3':
    print(f'Nmap Version: {scanner.nmap_version()}')
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print(f'Ip Status: {scanner[ip_addr].state()}')
    print(scanner[ip_addr].all_protocols())
    print(f'Open Ports: {scanner[ip_addr]["udp"].keys()}')
else:
    print('You\'ve entered an invalid selection. Please try again.')