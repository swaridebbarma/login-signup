import json

txt = "login and sign up"
x = txt.title()
print(x)



def signup():
    x={}
    y={}
    z=[]
    
    
    user1=input("enter any one option (login / sign up ):")
    username=input("enter your firstname:")
    username1=input("enter your lastname:")
    dob=input("enter your date of birth:")
    option=input("enter your (mble no or email):")
    gender=input("male/female/custom:")
    password=input("create new password:")
    
    c_l="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    s_l="abcdefghijklmnopqrstuvwxyz"

    no="0123456789"
    
    sp_ch="@#₹&!*$%¢€£©®"
    
    if len(password)>=8:
        a=0
        b=0
        c=0
        d=0
        i=0
        while i<len(password):
            if password[i] in c_l:
                a+=1
            elif password[i] in s_l:
                b+=1
            elif password[i] in no:
                c+=1
            elif password[i] in sp_ch:
                d+=1
            i+=1
            
        if a>=1 and b>=1 and c>=1 and d>=1:
            password1=input("confirm your password:")
            if password==password1:
                x["firstname"]=username
                x["lastname"]=username1
                x["date of birth"]=dob     
                x["mble no or email"]=option
                x["gender"]=gender
                x["password"]=password  
            
                z.append(x)

                y["users"]=x
    print("Congrats",username,"Successfully Resistered👍")

            
signup()

def login():
    if ["firstname"] in 