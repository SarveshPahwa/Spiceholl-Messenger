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
display()
t=input
#get in touch iwith teach tech team
print("3-Report a issue")
def issue():
    a=input("Enter a issue")
