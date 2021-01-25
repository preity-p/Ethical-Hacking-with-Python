# Ethical Hacking with Python

Ethical Hacking refers to the process of performing attacks on computer systems and networks to discover potential security weaknesses and help clients improve their security. It is common for ethical hackers to automate structured processes by writing their own scripts.

Python is a widely-used general-purpose, open-source, object-oriented HLL with libraries that can be used for hacking, making it ideal for implementing automation. Python's large community makes doubt resolution fast and easy.

This repository contains python3 scripts for automating basic tasks such as 

1. Setting up a TCP server-client pair
2. Brute-forcing protected passwords
3. Grabbing banners for reconnaissance
4. Keylogging
5. Automating network mapping (Implementing nmap)
6. OS fingerprinting
7. Port scanning

All instructions regarding customization have been provided in the scripts themselves.

## Installation

```bash
pip install python3-nmap
```

## Usage

1. OS fingerprinting

To run the script, open a terminal in the current directory and enter 

```bash
python os_fingerprint.py <target IP>
```

Here, <target IP> will be replaced by your target's IP address, and utilized as sys.argv[1] in the script. Before running the script, update the Environment Variables on your system

2. Keylogging

In this script, a metasploitable machine is used as the FTP server where the file with the pressed keys exist. The IP address of the machine needs to be the same as the address in the script. To setup a metasploitable machine, follow this tutorial:

https://www.thesecuritygeeks.com/security/install-metasploitable-2-in-virtual-box/

The default username and password are "msfadmin". The machine's IP address can be found out by running the "ifconfig" command on it. Make sure your virtual machine is online before running this script on your local machine.

After the script has finished running, run the "ls -a" command on the virtual machine to check if the keylogger results have been shared with it or not. The original .txt file will be in the same directory as the script, on your local machine, and its copy should be present in the metasploitable machine.

3. All other scripts can be accessed normally from a terminal, in the following manner:

```bash
python <filename.py>
```

## Contributing

Pull requests are welcome and encouraged. As this repository is for scripting and ethical hacking beginners, please explore further and improve the functionalities of these scripts as desired. Try writing new scripts for automating other penetration testing tasks as well.
