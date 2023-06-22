#-----------------------------------------------------------FUNCTIONS---------------------------------------------------------------#
import pickle
import os
def clearscreen():
    os.system('cls')
def createaccount():
    clearscreen()
    inertlogo()
    f=open("database1.dat","ab")
    f.close()
    f=open("messages.dat","ab")
    f.close()
    f=open("database1.dat","rb")
    try:
        checklist=[]
        while True:
            s=pickle.load(f)
            checklist.append(s[0][0])
    except:
        f.close()
    f=open("database1.dat","ab")    
    details=[]
    up=[]
    name=input("enter your fullname: ")
    while True:
        dob=input("enter your date of birth(in format DDMMYYYY): ")
        if len(dob)!=8:
            print("format didinot match")
        dob1=int(dob[2:4])
        dob2=int(dob[0:2])
        if(dob1<1 or dob1>12):
            print("enter a valid date of birth month")
        elif(dob2<0 or dob2>31):
            print("enter a valid date of birth date")
        else: break
    while True:
        cn=input("enter your contact no: ")
        if len(cn)!=10 or not cn.isdigit():
            print("Contact Number Didnot Match The Format")
        else:
            break
    while True:
        username=input("enter a suitable username ending with @spiceholl.com: ")        
        if not username.endswith("@spiceholl.com"):
            print("username doesnot endswith @spiceholl.com")
        elif username in checklist:
            print("username already exist")
        else: break    
    while True:
        password=input("enter a suitable password: ")
        cpassword=input("conferm password: ")
        if (cpassword==password):
            up.append(username)
            up.append(password)
            details.append(up)
            details.append(name)
            details.append(dob)
            details.append(cn)
            pickle.dump(details,f)
            clearscreen()
            print("Account created successfully")
            break
        else:
           print("password didnot matched")
    f.close()


def accountsearch():
    clearscreen()
    f=open("database1.dat","rb")
    a=[]
    global user
    user=input("                                                      Enter Your Username: ")
    password=input("                                                      Enter your password: ")
    a.append(user)
    a.append(password)
    flag=0
    try:
        while True:
            s=pickle.load(f)
            if(s[0]==a):
                global name
                name=s[1]
                flag=1
    except:
        f.close()
    if (flag==1):
        return name
    else:
        return 0


def recoverpassword():
    inertlogo()
    f=open("database1.dat","rb")
    o=open("database2.dat","ab")
    user_temp=input("Enter Your Username: ")
    cn=input("Enter Your Registered Mobile Numbe: ")
    flag=0
    try:
        while True:
            s=pickle.load(f)
            if s[0][0]==user_temp and s[3]==cn:
                while True:
                    print("Details Verified".center(130))
                    print("Username: ",s[0][0]," "*7,"Name: ",s[1]," "*7,"Comtact Number: ",s[2])
                    print()
                    p=input("Enter Your New Password: ")
                    cp=input("conferm Yor Password: ")
                    if(p==cp):
                        s[0][1]=cp
                        pickle.dump(s,o)
                        flag=1
                        break
                    elif(p!=cp):
                        clearscreen()
                        print("password didinot match ")
                        continue
            else:
               pickle.dump(s,o)
    except:
        f.close()
        o.close()
        os.remove("database1.dat")
        os.rename("database2.dat","database1.dat")
        if(flag==1):
            clearscreen()
            print("Account Recoverd Successfully Please Login With New Details")
        else:
           print("Account Not Found")


def displayfriend():
    inertlogo()
    flag=0
    f=open("database1.dat","rb")
    try:
        while True:
            s=pickle.load(f)
            if s[0][0]==user:
                flag=1
            else:
                print(s[0][0])
    except:
        f.close()


def messages(name):
    s=open("messages.dat","rb")
    print(name.center(130))
    print()
    try:
        while True:
            p=pickle.load(s)
            if((p[0]==user or p[0]==name) and (p[2]==user or p[2]==name)):
                if(p[0]==user):
                    print(" "*50,p[0],":",p[1])
                    print()
                else:
                    print(p[0],":",p[1])
                    print()
    except:
        s.close()


def chatting(name):
    while True:
        o=open("messages.dat","ab")
        a=[]
        mess=input("Enter Your Messages(Press enter to go back): ")
        if mess=="":
            break
        else:
            a.append(user)
            a.append(mess)
            a.append(name)
            pickle.dump(a,o)
            o.close()
            clearscreen()
            messages(name)
            print("Message Sent")
            continue
        


def deletemessages(name):
    print("-"*130)
    inertlogo()
    s=open("messages.dat","rb")
    f=open("messages1.dat","ab")
    flag=0
    try:
        while True:
            p=pickle.load(s)
            if((p[0]==user or p[0]==name) and (p[2]==user or p[2]==name)):
                flag=1
            else:
                pickle.dump(p,f)
    except:
        s.close()
        f.close()
        os.remove("messages.dat")
        os.rename("messages1.dat","messages.dat")


def deleteaccount():
    print("-"*150)
    inertlogo()
    s=open("database1.dat","rb")
    f=open("database2.dat","ab")
    flag=0
    try:
        while True:
            p=pickle.load(s)
            if(p[0][0]==user):
                flag=1
            else:
                pickle.dump(p,f)
    except:
        s.close()
        f.close()
        os.remove("database1.dat")
        os.rename("database2.dat","database1.dat")


def updateaccount():
    clearscreen()
    print("-"*130)
    inertlogo()
    s=open("database1.dat","rb")
    f=open("database2.dat","ab")
    try:
        while True:
            p=pickle.load(s)
            if(p[0][0]==user):
                print("Name: ",p[1]," "*10,"Date Of Birth: ",p[2]," "*10,"Conatct Number: ",p[3])
                name=input("Enter New Name(press enter to skip): ")
                while True:
                    if name=="": 
                        break
                    else:
                        p[1]=name
                        break
                while True:
                    dob=input("Enter New Date Of Birth In Format DDMMYYYY(press enter to skip): ")
                    if dob=="":
                        break
                    elif(len(dob)!=8):
                        print("Date Of Birth Didnot Match With the Format")
                    else:
                        p[2]=dob
                        break
                while True:
                    cn=input("Enter Your New Contact Number(press enter to skip): ")
                    if cn=="":
                        break
                    elif(len(cn)!=10 or not cn.isdigit()):
                        print("Contact Number Didnot Match The Format")
                    else:
                        p[3]=cn
                        break
                pickle.dump(p,f)

                
            else:
                pickle.dump(p,f)
    except:
        s.close()
        f.close()
        os.remove("database1.dat")
        os.rename("database2.dat","database1.dat")


def changepassword():
    print("-"*130)
    inertlogo()
    s=open("database1.dat","rb")
    f=open("database2.dat","ab")
    try:
        while True:
            p=pickle.load(s)
            if(p[0][0]==user):
                while True:
                    password=input("Enter New Password(Press enter to go back): ")
                    if(password==""):
                        pickle.dump(p,f)
                        break
                    elif(password!=""):
                         cpassword=input("Conferm password: ")
                         if password==cpassword:
                             p[0][1]=cpassword
                             pickle.dump(p,f)
                             print("Password Changed Successfully")
                             break
                         else:
                            print("Password Didnot Match")
                            continue
            else:
                pickle.dump(p,f)
    except:
        s.close()
        f.close()
        os.remove("database1.dat")
        os.rename("database2.dat","database1.dat")

def chatcommand():
    f=open("database1.dat","rb")
    try:
        checklist=[]
        while True:
            s=pickle.load(f)
            checklist.append(s[0][0])
    except:
        f.close()
    while True:
        displayfriend()
        global name
        name=input("Enter the name of friend to chat with(Press enter to go back): ")
        if(name in checklist):
            clearscreen()
            return name
            break
        elif(name==""):
            return 0
        else:
            clearscreen()
            print("-"*130)
            print("Enter a valid name")
            continue
            
                
def logo():
    from time import sleep
    print("Loading..... ")
    sleep(1.5)
    clearscreen()
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

def inertlogo():
    print(" "*111,"SPICEHOLL MESSENGER")

def display():
    import pickle
    o=open("database1.dat","rb")
    print("|","-"*107,"|")
    print("|","USERNAME"," "*31,"NAME"," "*21,"DOB"," "*13,"CONTACT NO."," "*9,"|")
    print("|","-"*107,"|")
    try:
        while True:
            s=pickle.load(o)
            print("|",s[0][0]," "*(38-len(s[0][0])),s[1]," "*(24-len(s[1])),s[2]," "*10,s[3]," "*10,"|")
            print("|","-"*107,"|")
    except:
        o.close()    
        

#----------------------------------------------------------User Interface-----------------------------------------------------------#
logo()
def ui():
    n=0
    n6=0
    c=0
    while True:
        print("-"*130)
        inertlogo()
        print("\033[1;31;40m 1-Create Account ".center(140))
        print("2-Log In".center(130))
        if(c!=0):
            print("3-Forgetton password".center(130))
        n=int(input("Enter Your Choice(Press any another key to exit): "))
        if n==1:
            createaccount()
        elif n==140303:
            while True:
                clearscreen()
                display()
                p=input("press enter to skip")
                if p=="":
                    clearscreen()
                    break
            
        elif(n==3):
            clearscreen()
            recoverpassword()
        elif(n==2):
            a=accountsearch()
            if(a==0):
                clearscreen()
                print("Account Not Found".center(130))
                c=c+1
            else:
                c=0
                clearscreen()
                print("Hello!!".center(130))
                print(a.center(130))
                while True:
                    print("-"*130)
                    inertlogo()
                    print("\033[1;32;40m1-Start Chatting")
                    print("2-Update Account Details")
                    print("3-Delete My Account")
                    print("4-Delete Chat History")
                    print("5-Change Password")
                    print("6-Log out")
                    n1=int(input("Enter Your Choice: "))
                    if n1==1:
                        while True:
                            clearscreen()
                            print("-"*130)
                            name=chatcommand()
                            if(name==0):
                                clearscreen()
                                break
                            else:
                                messages(name)
                                chatting(name)
                                n2=input("Want To Continue Chatting,(Enter Y for Yes or N For No): ")
                                if n2 in "yY": continue
                                                                            
                                clearscreen()
                                break
                    elif n1==2:
                        updateaccount()
                        clearscreen()          
                                      
                        print("Update successful".center(130))
                    elif n1==3:
                        clearscreen()
                        print(user.center(130))
                        print()
                        n3=input("Are You sure You Want To Delete Account,(Enter Y for Yes or N For No): ")
                        if n3=="":
                           clearscreen()      
                        elif(n3 in"yY"):
                            deleteaccount()
                            clearscreen()
                            break
                        else:
                            clearscreen()
                    elif n1==4:
                        while True:
                            clearscreen()
                            print("-"*130)
                            displayfriend()
                            name=input("Enter The Name Of Friend With Whom You Want Delete Your Chat(Press enter to go back): ")
                            if(name==""):
                                clearscreen()
                                break
                            else:
                               messages(name)
                               print("Are You Sure You Want To Delete Your Chat History With",name)
                               n4=input("enter y for yes and n for no: ")
                               if n4 in "Yy":
                                    deletemessages(name)
                                    clearscreen()  
                                    print("Chat History Deleted Now",name,"Also Will Not Be Able Access Chats With You")
                                    break                        
                    elif n1==5:
                        clearscreen()
                        changepassword()
                        clearscreen()
                        print("password changed successfully")          
                    elif n1==6:
                         clearscreen()
                         break
                    else:
                        clearscreen()
                        print("Invalid Input")        

        else:
            break
ui()   
    
