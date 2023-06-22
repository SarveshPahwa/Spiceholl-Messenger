#-----------------------------------------------------------FUNCTIONS---------------------------------------------------------------#

import mysql.connector
import os
import time
def clearscreen():
    os.system('cls')
def createaccount():
    clearscreen()
    inertlogo()
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="spahwa")
    mycur=mydb.cursor()
    sql="select username from profile"
    mycur.execute(sql)
    checklist=mycur.fetchall()    
    details=()
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
        ustry=(username,)
        if not username.endswith("@spiceholl.com"):
            print("username doesnot endswith @spiceholl.com")
        elif ustry in checklist:
            print("username already exist")
        else: break    
    while True:
        password=input("enter a suitable password: ")
        cpassword=input("conferm password: ")
        if (cpassword==password):
            dob1=dob[2:4]
            dob2=dob[0:2]
            dob3=dob[4:8]
            dobf=dob3+"-"+dob1+"-"+dob2
            cn1=int(cn)
            details=(username,password,name,dobf,cn1)
            sql="insert into profile values (%s,%s,%s,%s,%s)"
            mycur.execute(sql,details)
            mydb.commit()
            clearscreen()
            print("Account created successfully")
            break
        else:
           print("password didnot matched")

def accountsearch():
    clearscreen()
    a=()
    global user
    user=input("                                                      Enter Your Username: ")
    password=input("                                                      Enter your password: ",)
    a=(user,password)
    flag=0
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="spahwa")
    mycur=mydb.cursor()
    sql="select username,password from profile"
    mycur.execute(sql)
    check=mycur.fetchall()
    if a in check:
        flag=1
        sql="select name from profile where username=(%s)"
        user1=(user,)
        mycur.execute(sql,user1)
        name1=mycur.fetchone()
        global name
        name=name1[0]
    if (flag==1):
        return name
    else:
        return 0

def recoverpassword():
    user_temp=input("Enter Your Username: ")
    user1=(user_temp,)
    cn=int(input("Enter Your Registered Mobile Numbe: "))
    a=(user_temp,cn)
    flag=0
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="spahwa")
    mycur=mydb.cursor()
    sql="select username,contact_number from profile"
    mycur.execute(sql)
    check=mycur.fetchall()
    if a in check:
        clearscreen()
        sql="select username,name,contact_number from profile where username=(%s)"
        mycur.execute(sql,user1)
        s=mycur.fetchone()
        while True:
            print("Details Verified".center(130))
            print("Username: ",s[0]," "*7,"Name: ",s[1]," "*7,"Comtact Number: ",s[2])
            p=input("Enter Your New Password: ")
            cp=input("conferm Yor Password: ")
            if(p==cp):
                sql="update profile set password=(%s) where username=(%s)"
                val=(cp,user_temp)
                mycur.execute(sql,val)
                mydb.commit()
                flag=1
                break
            elif(p!=cp):
                clearscreen()
                print("password didinot match ")
                continue
        if(flag==1):
            clearscreen()
            print("Account Recoverd Successfully Please Login With New Details")
    else:
        clearscreen()
        print("Account Not Found")


def chatcommand():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="spahwa")
    mycur=mydb.cursor()
    sql="select username from profile"
    mycur.execute(sql)
    checklist=mycur.fetchall()
    while True:
        displayfriend()
        global name
        name=input("Enter the name of friend to chat with(Press enter to go back): ")
        name1=(name,)
        if name1 in checklist:
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

def displayfriend():
    inertlogo()
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="spahwa")
    mycur=mydb.cursor()
    flag=0
    sql="select username from profile"
    mycur.execute(sql)
    test=mycur.fetchall()
    for i in test:
        if i[0]==user:
            flag=1
        else:
            print(i[0])

def messages(name):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="spahwa")
    mycur=mydb.cursor()
    print(name.center(130))
    print()
    sql="select * from messages where sender in(%s,%s) and reciever in(%s,%s)"
    val=(user,name,user,name)
    mycur.execute(sql,val)
    test=mycur.fetchall()
    for i in test:
        if(i[0]==user):
            print(" "*50,i[0],":",i[1])
            print()
        else:
            print(i[0],":",i[1])

def chatting(name):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="spahwa")
    mycur=mydb.cursor()
    
    while True:
        val=()
        mess=input("Enter Your Messages(Press enter to go back): ")
        if mess=="":
            break
        else:
            sql="insert into messages values(%s,%s,%s)"
            val=(user,mess,name)
            mycur.execute(sql,val)
            mydb.commit()
            clearscreen()
            messages(name)
            print("Message Sent")
            continue

def deletemessages(name):
    print("-"*130)
    val=()
    inertlogo()
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="spahwa")
    mycur=mydb.cursor()
    sql="delete from messages where sender in(%s,%s) and reciever in(%s,%s)"
    val=(user,name,user,name)
    mycur.execute(sql,val)
    mydb.commit()

def deleteaccount():
    print("-"*150)
    inertlogo()
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="spahwa")
    mycur=mydb.cursor()
    val=()
    sql="delete from profile where username=(%s)"
    val=(user,)
    mycur.execute(sql,val)
    mydb.commit()
    sql="delete from messages where sender=(%s) or reciever=(%s)"
    val=(user,user)
    mycur.execute(sql,val)
    mydb.commit()
    

def updateaccount():
    val=()
    clearscreen()
    print("-"*130)
    inertlogo()
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="spahwa")
    mycur=mydb.cursor()
    sql="select * from profile where username=(%s)"
    val=(user,)
    mycur.execute(sql,val)
    p=mycur.fetchone()
    print("Name: ",p[2]," "*10,"Date Of Birth: ",p[3]," "*10,"Conatct Number: ",p[4])
    name=input("Enter New Name(press enter to skip): ")
    while True:
        if name=="":
            break
        else:
            sql="update profile set name=(%s) where username=(%s)"
            val=(name,user)
            mycur.execute(sql,val)
            mydb.commit()
            break
    while True:
        dob=input("Enter New Date Of Birth In Format DDMMYYYY(press enter to skip): ")
        if dob=="":
            break
        elif(len(dob)!=8):
            print("Date Of Birth Didnot Match With the Format")
        else:
            sql="update profile set dob=(%s) where username=(%s)"
            dob1=dob[2:4]
            dob2=dob[0:2]
            dob3=dob[4:8]
            dobf=dob3+"-"+dob1+"-"+dob2
            val=(dobf,user)
            mycur.execute(sql,val)
            mydb.commit()
            break
    while True:
        cn=input("Enter Your New Contact Number(press enter to skip): ")
        if cn=="":
            break
        elif(len(cn)!=10 or not cn.isdigit()):
            print("Contact Number Didnot Match The Format")
        else:
            sql="update profile set contact_number=(%s) where username=(%s)"
            cn1=int(cn)
            val=(cn1,user)
            mycur.execute(sql,val)
            mydb.commit()
            break

def changepassword():
    val=()
    print("-"*130)
    inertlogo()
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="spahwa")
    mycur=mydb.cursor()
    while True:
        password=input("Enter New Password(Press enter to go back): ")
        if(password==""):
            break
        elif(password!=""):
            cpassword=input("Conferm password: ")
            if password==cpassword:
                sql="update profile set password=(%s) where username=(%s)"
                val=(cpassword,user)
                mycur.execute(sql,val)
                mydb.commit()
                print("Password Changed Successfully")
                break
            else:
                print("Password Didnot Match")
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
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="spahwa")
    mycur=mydb.cursor()
    print("|","-"*107,"|")
    print("|","USERNAME"," "*31,"NAME"," "*21,"DOB"," "*13,"CONTACT NO."," "*9,"|")
    print("|","-"*107,"|")
    sql="select * from profile"
    mycur.execute(sql)
    test=mycur.fetchall()
    for i in test:
        print("|",i[0]," "*(38-len(i[0])),i[2]," "*(24-len(i[2])),i[3]," "*8,i[4]," "*10,"|")
        print("|","-"*107,"|")
   
#----------------------------------------------------------User Interface-----------------------------------------------------------#
logo()
def ui():
    n=0
    n6=0
    c=0
    while True:
        print("-"*130)
        inertlogo()
        print("\033[1;33;40m 1-Create Account ".center(140))
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
                    print("1-Start Chatting")
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
