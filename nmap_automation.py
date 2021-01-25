import nmap

scanner= nmap.PortScanner()
print("---------------NMAP Automation---------------")
print("---------------------------------------------")

ip= input("Please enter the IP address you wish to scan: ")
print("The IP address you entered is: ", ip)
type(ip)

scan_no= input("""\nPlease enter the type of scan you wish to run
                1. SYN ACK Scan
                2. UDP Scan
                3. Comprehensive Scan\n""")

print("Scan number ", scan_no, " is going to be conducted.")

if scan_no== '1':
    print("Version: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sS')                            # 1-1024 is the range of ports to be scanned
    print("Method: ", scanner.scaninfo()['tcp']['method'])
    print("Services: ", scanner.scaninfo()['tcp']['services'])
    print("IP status: ", scanner[ip].state())
    print("Open ports: ", scanner[ip]['tcp'].keys())
elif scan_no== '2':
    print("Version: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sU')
    print("Method: ", scanner.scaninfo()['udp']['method'])
    print("Services: ", scanner.scaninfo()['udp']['services'])
    print("IP status: ", scanner[ip].state())
    print("Open ports: ", scanner[ip]['udp'].keys())
elif scan_no== '3':
    print("Version: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sS -sV -sC -A -O')
    print("Method: ", scanner.scaninfo()['tcp']['method'])
    print("Services: ", scanner.scaninfo()['tcp']['services'])
    print("IP status: ", scanner[ip].state())
    print("Open ports: ", scanner[ip]['tcp'].keys())
else:
    print("Please enter a valid option.")

"""
FLAG LIST

-v              Increase the verbosity level
-sS         	TCP SYN port scan
-sU             UDP port scan
-sV             Determines the version of the service running on port
-sC             Scan with default NSE scripts
-A              OS detection, version detection, script scanning, and traceroute
-O              Remote OS detection using TCP/IP stack fingerprinting

"""