import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def clear_screen():
    command = "cls"
    subprocess.call(command,shell=True)  
def logo():
    from time import sleep
    sleep(1.5)
    print(" "*53,"|"*26)
    sleep(0.5)
    print(" "*53,"|"," "*7,"$"*7," "*6,"|")
    sleep(0.5)
    for i in range(0,3):
        print(" "*53,"|"," "*6,"$"," "*13,"|")
        sleep(0.05)
    print(" "*53,"|"," "*7,"$"*7," "*6,"|")
    sleep(0.5)
    for i in range(0,3):
        print(" "*53,"|"," "*14,"$"," "*5,"|")
        sleep(0.05)
    print(" "*53,"|"," "*7,"$"*7," "*6,"|")
    sleep(0.5)
    print(" "*53,"|  ","SPICEHOLL MESSENGER ","|")
    sleep(0.5)
    print(" "*53,"|"*26)
    clear_screen()
def inertlogo():
    print(" "*111,"SPICEHOLL MESSENGER")
def starter():
    from time import sleep
    print("Please Wait loading page")
    for i in range(0,130):
        print("|",end="")
        sleep(0.001)
       
logo()        
starter()

        

