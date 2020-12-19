import nmap
import sys
import time

nm_scan = nmap.PortScanner()

print('\n Running \n')
nm_scanner= nm_scan.scan(sys.argv[1],'80',arguments='-O')    # OS fingerprinting at port 80 of target IP obtained using sys.argv[1]

# Run nmap on your console to check all parameters. Choose appropriate parameters and include them in the code.
# Host status, port status, method of scanning and target OS parameters have been included below

host_status= "The host is: " +nm_scanner['scan'][sys.argv[1]]['status']['state']+".\n"
port_status= "Port 80 is: " +nm_scanner['scan'][sys.argv[1]]['tcp'][80]['state']+".\n"
scan_method= "The method of scanning is: " +nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason']+".\n"
os_guess= "There is a %s percent chance that the host is running %s"%(nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy'], nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['name'])+".\n"

# Generates timestamp for the report

with open("%s.txt"%sys.argv[1], 'w') as f:
    f.write(host_status+port_status+scan_method+os_guess)
    f.write("\nReport generated at: "+time.strftime("%Y-%m-%d_%H:%M:%S GMT", time.gmtime()))

print("\n Finished scan. Check results in \'"+sys.argv[1]+".txt\'.")