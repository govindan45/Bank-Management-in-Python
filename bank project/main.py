from pymysql import *
import datetime as dt
con=connect(host="localhost",user="root",password="Arun@12345",database="bankmanage")

print("Connected")
while(True):
    print("==========WELCOME OUR BANK===========")
    print(print(dt.datetime.now()))
    print('1.REGISTER')
    print()
    print('2.LOGIN')
    print()
    print('3.Exit')
    print()
    choi=int(input("Enter Your Choice: "))

    if(choi==1):
        name=input('Enter a Username=')
        passwd=input('Enter a 4 DIGIT Password=')
        print()
        if(len(passwd)==4):
            p="INSERT  INTO user values ('{0}','{1}')".format(name,passwd)
            a=con.cursor()
            a.execute(p)
            con.commit()
            print('USER created succesfully')
            import menu
        else:
            print("Please Enter Only 4 Digit Password Only")
    elif(choi==2):
        while(True):
            name=input('Enter your Username=')
            print()
            passwd=input('Enter your 4 DIGIT Password=')
            q="select * from user where cname='{0}' and pin='{1}'".format(name,passwd)
            a=con.cursor()
            a.execute(q)
            c=a.fetchall()
            for i in c:
                for j in i:
                    cname=j
            if len(c)!=0:
                print("Login success")
                print()
                import menu
                break
            else:
                print("Login Unsuccess")
                print()
            
    elif(choi==3):
        print("Thankyou")
        break
    else:
        print("Invalid Option")
    