from pymysql import *
import datetime 
import random
from email.message import EmailMessage
import ssl
import smtplib
con=connect(host="localhost",user="root",password="Arun@12345",database="bankmanage")

while(True):
        print()
        print('1.CREATE BANK ACCOUNT')
        print()
        print('2.TRANSACTION')
        print()
        print('3.PIN CHANGE')
        print()
        print('4.TRANSACTION DETAILS')
        print()
        print('5.DELETE ACCOUNT')
        print()
        print('6.QUIT')
        print()
        choi=int(input("Enter Your Choice: "))
        if(choi==1):
            date=datetime.datetime.now()
            time=datetime.datetime.now()
            datep=date.strftime("%y-%m-%d")
            timep=time.strftime("%H:%M")
            cname=input("Enter Your Name: ")
            phno=int(input("Enter your Phone Number: "))
            pin=input("Enter Your New pin: ")
            while(True):
                if(len(pin)==4):
                    mail=input("Enter Your Email id: ")
                    acccreated_date=datep
                    acccreated_time=timep
                    bal=int(input("Enter a Initial Deposit Amount: "))
                    print("---------------------------------------------")
                    acc=random.randrange(1000000, 9999999)
                    print("Please Note Your Account Number: ")
                    print("Your Account Number is: ",acc)
                    print("----DO NOT FORGET YOUR ACCOUNT NUMBER----")
                    accno=int(input("Please Enter Your Account Number: "))
                    q="insert into customer values('{0}','{1}','{2}','{3}','{4}','{5}','{6}',{7})".format(accno,cname,phno,pin,mail,acccreated_date,acccreated_time,bal)
                    a=con.cursor()
                    a.execute(q)
                    con.commit()
                    print("Account Created Succesfully")
                    print("------------------------------")
                    print()
                    break
                else:
                    print("PIN Enter Only 4 Digit")
                    print("-------------------------")
                    print()
        if(choi==2):
            accno=int(input('Enter Your Account Number='))
            print()
            a=con.cursor()
            p="select * from customer where accno='{0}'".format(accno)
            a=con.cursor()
            a.execute(p)
            data=a.fetchall()
            count=a.rowcount
            print(count)
        
            con.commit()
            if count == 0:
                print()
                print('Account Number Invalid Sorry Try Again Later')
                print("---------------------------------------------")
                print()
            else:
                print()
                print('1.WITHDRAW AMOUNT')
                print()
                print('2.Deposit AMOUNT')
                print()

                print()
                x=int(input('Enter your CHOICE='))
                print()
                if(x==1):
                    amt=int(input("Enter Your Withdraw amount: "))
                    q="select bal from customer where accno='{0}'".format(accno)
                    a=con.cursor()
                    a.execute(q)
                    bal=a.fetchall()
                    for i in bal:
                        for j in i:
                            cbal=j
                            print(cbal)

                    if(cbal>=amt):
                        d=0
                        date=datetime.datetime.now()
                        time=datetime.datetime.now()
                        datep=date.strftime("%y-%m-%d")
                        timep=time.strftime("%H:%M")
                        ubal=cbal-amt
                        uc="update customer set bal='{0}' where accno={1}".format(ubal,accno)
                        a=con.cursor()
                        a.execute(uc)
                        tc="INSERT  INTO transactions values ('{0}' , '{1}' , '{2}' , '{3}') ".format(accno,datep,amt,d)
                        a=con.cursor()
                        a.execute(tc)
                        con.commit()
                        print()
                        print('Withdraw Succesfully!!!!!')
                        print("----------------------------")
                        print()
                if(x==2):
                    w=0
                    amt=int(input("Enter Your Deposit amount: "))
                    q="select bal from customer where accno='{0}'".format(accno)
                    a=con.cursor()
                    a.execute(q)
                    bal=a.fetchall()
                    for i in bal:
                        for j in i:
                            cbal=j
                            
                    date=datetime.datetime.now()
                    time=datetime.datetime.now()
                    datep=date.strftime("%y-%m-%d")
                    timep=time.strftime("%H:%M")
                    ubal=cbal+amt
                    uc="update customer set bal='{0}' where accno={1}".format(ubal,accno)
                    a=con.cursor()
                    a.execute(uc)
                    tc="INSERT  INTO transactions values ('{0}' , '{1}' , '{2}' , '{3}') ".format(accno,datep,w,amt)
                    a=con.cursor()
                    a.execute(tc)
                    con.commit()
                    print()
                    print('Deposit Succesfully!!!!!')
                    print("--------------------------")
                    print()
        if(choi==3):
            accno=int(input("ENter Your Account Number: "))
            otp=random.randrange(1000, 9999)
            bal="select mail from customer where accno='{0}'".format(accno)
            a=con.cursor()
            a.execute(bal)
            c=a.fetchall()
            for i in c:
                for j in i:
                    cm=j

            email_sender="govindangk44@gmail.com"
            email_password="ugqz wceq fkos fkjx"

            email_receiver=cm

            subject="OTP"
            body="{0}".format(otp)

            em=EmailMessage() 
            em['From']=email_sender
            em['To']=email_receiver
            em['Subject']=subject

            em.set_content(body)

            context=ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
                smtp.login(email_sender,email_password)
                smtp.sendmail(email_sender,email_receiver,em.as_string())
            print("OTP Send Succesfully!!!")
            print("-------------------------")
            cotp=int(input("Enter OPT: "))
            while(True):
                if(otp==cotp):
                    newpin=int(input("Enter Your New Pin: "))
                    bale="update customer set pin='{0}' where accno={1}".format(newpin,accno)
                    b=con.cursor()
                    b.execute(bale)
                    con.commit()
                    print("PIN Change Succesfully!!!")
                    print("------------------------")
                    break
                else:
                    print("OTP is INCORRECT!!")
                    print("------------------------")
        if(choi==4):
            accno=int(input('Enter your account number='))
            print()
            b=con.cursor()
            b.execute("select * from customer where accno='{0}'".format(accno) )
            if b.fetchone() is  None:
                print()
                print('Invalid Account number')
                print("------------------------")
                print()
            else:
                b=con.cursor()
                b.execute("select * from transactions where acct_no='{0}'".format(accno))
                data=b.fetchall()
                for row in data:
                    print('ACCOUNT NO=',accno)
                    print()
                    print('DATE=',row[1])
                    print()
                    print('WITHDRAWAL AMOUNT=',row[2])
                    print()
                    print('DEPOSIT AMOUNT=',row[3])
                    print("------------------------------")
                    print()
                print("This Your Transcation History!!")
                print("------------------------------")
        if(choi==5):
            print('DELETE YOUR ACCOUNT')
            accno=int(input('Enter your account number='))
            b=con.cursor()
            b.execute("delete from customer where accno='{0}'".format(accno) )
            con.commit()
            print('ACCOUNT DELETED SUCCESFULLY')
            print("---------------------------------")
            print()
        if(choi==6):
            print("Thank You!!!")
            break
    
