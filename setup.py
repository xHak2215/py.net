import os
from zipfile import ZipFile 

mein_direct=str(os.path.dirname(os.path.abspath(__name__)))
mein_direct.encode("utf-8")
os.chdir(mein_direct)

with ZipFile("Winpcap_Install-master.zip", 'r') as zip: 
    # printing all the contents of the zip file 
    zip.printdir() 
    zip.extractall()
os.chdir(mein_direct+"//Winpcap_Install-master")
os.system("start Install_WinPcap.bat")
os.chdir(mein_direct)
os.system("pip install -r requirements.txt")