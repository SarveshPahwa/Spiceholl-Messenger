import pickle
import os

def createaccount():
    inertlogo()
    f=open("database1.dat","ab")
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
    name=input("enter your fullname- ")
    while True:
        dob=input("enter your date of birth(in format DDMMYYYY)- ")
        dob1=int(dob[2:4])
        dob2=int(dob[0:2])
        if len(dob)!=8:
            print("format didinot match")
        elif(dob1<1 or dob1>12):
            print("enter a valid date of birth month")
        elif(dob2<0 or dob2>31):
            print("enter a valid date of birth date")
        else: break
    while True:
        cn=input("enter your contact no- ")
        if len(cn)!=10 or not cn.isdigit():
            print("Contact Number Didnot Match The Format")
        else:
            break
    while True:
        username=input("enter a suitable username ending with @spiceholl.com- ")        
        if not username.endswith("@spiceholl.com"):
            print("username doesnot endswith @spiceholl.com")
        elif username in checklist:
            print("username already exist")
        else: break    
    while True:
        password=input("enter a suitable password- ")
        cpassword=input("conferm password- ")
        if (cpassword==password):
            up.append(username)
            up.append(password)
            details.append(up)
            details.append(name)
            details.append(dob)
            details.append(cn)
            pickle.dump(details,f)
            print("Account created successfully")
            break
    else:
        print("password didnot matched enter details again")
    f.close()


def accountsearch():
    f=open("database1.dat","rb")
    a=[]
    global user
    user=input("Enter Your Username- ")
    password=input('Enter your password- ')
    a.append(user)
    a.append(password)
    flag=0
    try:
        while True:
            s=pickle.load(f)
            if(s[0]==a):
                flag=1
    except:
        f.close()
    if (flag==1):
        return 1
    else:
        return 0


def recoverpassword():
    inertlogo()
    f=open("database1.dat","rb")
    o=open("database2.dat","ab")
    user_temp=input("Enter Your Username- ")
    cn=input("Enter Your Registered Mobile Number- ")
    flag=0
    try:
        while True:
            s=pickle.load(f)
            if s[0][0]==user_temp and s[3]==cn:
                print("Details Verified")
                p=input("Enter Your New Password- ")
                cp=input("conferm Yor Password- ")
                if(p==cp):
                    s[0][1]=cp
                    pickle.dump(s,o)
                    flag=1
            else:
               pickle.dump(s,o)
    except:
        f.close()
        o.close()
        os.remove("database1.dat")
        os.rename("database2.dat","database1.dat")
        if(flag==1):
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
    s=open("messages.dat","ab")
    while True:
        a=[]
        mess=input("Enter Your Messages")
        a.append(user)
        a.append(mess)
        a.append(name)
        pickle.dump(a,s)
        print("Message Sent")
        b=input("Want To Send More Messages(enter y for yes n for no)")
        if b in "yY":
            continue
        else:
            break
    s.close()    


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
    print("-"*130)
    inertlogo()
    s=open("database1.dat","rb")
    f=open("database2.dat","ab")
    try:
        while True:
            p=pickle.load(s)
            if(p[0][0]==user):
                print(p[1],p[2],p[3])
                name=input("Enter New Name(press enter to skip)")
                while True:
                    if name=="": 
                        break
                    else:
                        p[1]=name
                        break
                while True:
                    dob=input("Enter New Date Of Birth In Format DDMMYYYY(press enter to skip)")
                    if dob=="":
                        break
                    elif(len(dob)!=8):
                        print("Date Of Birth Didnot Match With the Format")
                    else:
                        p[2]=dob
                        break
                while True:
                    cn=input("Enter Your New Contact Number(press enter to skip)")
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
                    password=input("Enter New Password")
                    cpassword=input("Conferm password")
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

def logo():
    print(" "*53,"|"*26)
    print(" "*53,"|"," "*7,"$"*7," "*6,"|")
    for i in range(0,3):
        print(" "*53,"|"," "*6,"$"," "*13,"|")
    print(" "*53,"|"," "*7,"$"*7," "*6,"|")
    for i in range(0,3):
        print(" "*53,"|"," "*14,"$"," "*5,"|")
    print(" "*53,"|"," "*7,"$"*7," "*6,"|")
    print(" "*53,"|  ","SPICEHOLL MESSENGER ","|")
    print(" "*53,"|"*26)

def inertlogo():
    print(" "*111,"SPICEHOLL MESSENGER")
        

#----------------------------------------------------------User Interface-----------------------------------------------------------#
logo()
def ui():
    n=0
    c=0
    while True:
        print("-"*130)
        inertlogo()
        print("1-Create Account".center(130))
        print("2-Log In".center(130))
        if(c!=0):
            print("3-Forgetton password".center(130))
        n=int(input("Enter Your Choice"))
        if n==1:
            createaccount()
        elif(n==3):
            recoverpassword()
        elif(n==2):
            a=accountsearch()
            if(a==0):
                print("Account Not Found")
                c=c+1
            elif(a==1):
                c=0
                print(' '*55,"Hello",user)
                while True:
                    print("-"*130)
                    inertlogo()
                    print("1-Start Chatting")
                    print("2-Update Account Details")
                    print("3-Delete My Account")
                    print("4-Delete Chat History")
                    print("5-Change Password")
                    print("6-Log out")
                    n1=int(input("Enter Your Choice"))
                    if n1==1:
                        while True:
                            print("-"*130)
                            displayfriend()
                            name=input("Enter The Name Of Friend To Chat With")
                            messages(name)
                            chatting(name)
                            n2=input("Want To Continue Chatting,(Enter Y for Yes or N For No)")
                            if n2 in "yY": continue
                            else: break
                    elif n1==2:
                        updateaccount()
                        print("Update successful".center(130))
                    elif n1==3:
                        n3=input("Are You sure You Want To Delete Account,(Enter Y for Yes or N For No)")
                        if n3 in"yY":
                            deleteaccount()
                            break
                    elif n1==4:
                        while True:
                            displayfriend()
                            name=input("Enter The Name Of Friend With Whom You Want Delete Your Chat")
                            messages(name)
                            print("Are You Sure You Want To Delete Your Chat History With",name)
                            n4=input("enter y for yes and n for no")
                            if n4 in "Yy":
                                deletemessages(name)
                                print("Chat History Deleted Now",name,"Also Will Not Be Able Access Chats With You")
                                break                        
                    elif n1==5:
                        changepassword()
                    elif n1==6:
                        break
                    else:
                        print("Invalid Input")        

ui()   
                

                
