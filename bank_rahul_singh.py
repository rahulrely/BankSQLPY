######################      Import     #########################
import datetime as dt
import time
import random as rd
####################      date          ########################
t=dt.date.today()
r_num=123
################################################################
d_ac=[]     #account number list

d_cn=[]     #consumer number list

d_name=[]   #name of ac holders

d_dob=[]    #date of birth of ac holders

d_fname=[]  #father's name of ac holders

d_mname=[]  #mother's name of ac holders

d_address=[]#address of ac holders

d_balance=[]#balance of ac holders

d_transaction=[] # all transaction 

l_user=[] # all username
####################     database     ###########################
import mysql.connector as sql
pd=input("Enter the Database Password :")
q=sql.connect(host="localhost",user="root",passwd=pd)
if q.is_connected():
    print("--------------------- Database is Conneted -----------------------")
else:
    print("###### Failed to Connect Database ########")
cusr=q.cursor()

cusr.execute("CREATE DATABASE IF NOT EXISTS dbpyprojectrahul")

cusr.execute("USE dbpyprojectrahul")

comd='''CREATE TABLE IF NOT EXISTS customers (ACCOUNT_NUMBER BigInt PRIMARY KEY,CONSUMER_NO BigInt not null unique,
NAME VARCHAR(100) not null,DOB VARCHAR(45) not null,FatherName VARCHAR(100) not null,MotherName VARCHAR(100) not null,
Address VARCHAR(100) not null,USER VARCHAR(20) NOT NULL UNIQUE,PASS VARCHAR(20))'''

cusr.execute(comd)

##############      statement        #############################
def passbook(bk,ac,ifc,un,cn,dob,fn,mn,t,address):
    print("_________________________________________________________________________")
    print()
    print("------------------------------",bk,"-------------------------------------",sep="")
    print()
    print("=========================================================================")
    print("Account No. -",ac,end="")
    print("                     IFSC -",ifc)
    print("Name -",un,end="")
    print("                     Consumer No. -",cn)
    print("Date Of Birth -",dob)
    print("Father's Name -",fn)
    print("Mother's Name -",mn,)
    print("Address -",address)
    print("Branch Location - This PC",end="")
    print("                     Date Of Account Created -",t)
    print()
    print("_________________________________________________________________________")
    
################################################################
def username(consumer,dob,ac):
    print("_________________________________________________________________________")
    print()
    print("Your Default Username is Consumer Number")
    print("-------------------------------------------------------------------------")
    ask=input("Enter username to change it (if not then skip) :")
    check=len(ask)
    if(check!=0):
        print("-------------------------------------------------------------------------")
        ask1=input("Enter Your Current Username :")
        print("-------------------------------------------------------------------------")
        ask2=input("Enter Your Account Number :")
        print("-------------------------------------------------------------------------")
        ask3=input("Enter Your Date Of Birth(YYYY-MM-DD) :")
        print("-------------------------------------------------------------------------")
        if(ask3==dob and ask1==consumer and ask2==ac):
            consumer=ask
            print("Your Username Sucessfully Changed.")
            print("_________________________________________________________________________")
            print()
        else:
            print("Wrong Username or Date Of Birth or Account Number")
        print("_________________________________________________________________________")
        print()
    return consumer
################################################################
def password(r_num,ac,cn,consumer,dob):
    ask_num=int(input("Enter the Password Create/Change Referal number(ask to admin(123)) :"))
    if(ask_num==r_num):
        print("_________________________________________________________________________")
        print()
        u_name=input("Enter your Username to Create/Change Password :")
        print("-------------------------------------------------------------------------")
        ask1=input("Enter Your Date of Birth(YYYY-MM-DD):")
        print("-------------------------------------------------------------------------")
        ask2=input("Enter Your Consumer Number :")
        print("-------------------------------------------------------------------------")
        ask3=input("Enter Your Account Number :")
        print("-------------------------------------------------------------------------")
        if(u_name==consumer and ask1==dob and ask2==cn and ask3==ac):
            p_name=input("Enter your Password :")
            print("-------------------------------------------------------------------------")
            print("Password Succesfuly Changed/Created.")
            print("_________________________________________________________________________")
            print()
            return p_name
        else:
            print("Username Wrong :(")
            print("_________________________________________________________________________")
            print()
    else:
        print("Wrong referal number :(")
##################      login Check      ############################
def login(u_list):
    print()
    u_name=input("Enter the Username :")
    if u_name in u_list:
        print()
        p_word=input("Enter the Password :")
        print()
        CD="SELECT PASS FROM customers WHERE USER='{}'".format(p_word)
        cusr.execute(CD)
        duci=cusr.fetchone()
        if(p_word==duci[0]):
            print("Login Sucessful :)")
            login_sucess=1
        else:
            print("Password Wrong :( ")
            login_sucess=0
    else:
        print("Username Wrong OR User Not Found !")
        login_sucess=0
    return login_sucess,u_name
#######################   transaction    ############################
def transaction(AC):
    xx=len(AC)
    if(xx!=0):
        print("=====================================================================================")
        print("Sr. No.","Type","Date","Amount","Available","Remark",sep="        ")
        print()
        #sql
        com9="select * from transaction WHERE USER = '{}' ".format(AC)
        cusr.execute(com9)
        tra=cusr.fetchall()
        x=len(tra)
        for i in tra:
            for j in i:
                print(j,end="")
            print()
        print()
        print()
    else:
        print("No Transaction to show")
#######################    countdown    ############################
def countdown(t): 
    while t:
        mins, secs = divmod(t, 60) 
        a='{:02d}:{:02d}'.format(mins,secs)
        print(a)
        time.sleep(1)
        t-=1
    print('Page timeout successfull')
###########################  remark   ##########################
def remark():
    b=input("Enter Remark (if any) :")
    n=len(b)
    if(n==0):
        b="No Remark"
    return b
#################   main code starts     #######################
ifsc="IN012345"
bankname="BANK OF INDIA"
print()
print("**********************************************************************************************")
print("                                   ",bankname,"                                   ")
print("Branch Location - This PC",end="      ")
print("Date -",t,end="       ")
print("IFSC -",ifsc)
print()

ask=input("Enter 'Y' to Open a New Account(if not then skip) :")
print()
n=0
while(ask=="Y" or ask=="y"):
    ask="changed the value to stop loop"
    
    n_ac=rd.randint(5400070000,9990099999)
    ac=str(n_ac)
    d_ac.append(ac)
    
    n_cn=rd.randint(467476,999999)
    cn=str(n_cn)
    d_cn.append(cn)

    print("-------------------------------------------------------------------------")
    name=input("Enter your Name : ")
    print("-------------------------------------------------------------------------")
    d_name.append(name)
    print()

    print("-------------------------------------------------------------------------")
    dob=input("Enter your Date Of Birth(YYYY-MM-DD) : ")
    print("-------------------------------------------------------------------------")
    d_dob.append(dob)
    print()

    print("-------------------------------------------------------------------------")
    fname=input("Enter your Father's Name : ")
    print("-------------------------------------------------------------------------")
    d_fname.append(fname)
    print()

    print("-------------------------------------------------------------------------")
    mname=input("Enter your Mother's Name : ")
    print("-------------------------------------------------------------------------")
    d_mname.append(mname)
    print()

    print("-------------------------------------------------------------------------")
    address=input("Enter your Present Address : ")
    print("-------------------------------------------------------------------------")
    d_address.append(address)
    print()

    print("Your Account Sucessfully Created.")
    print()
    print("-------------------------------------------------------------------------")
    print("Your Account Number is",ac,"       ","Your Consumer Number is",cn)
    print("-------------------------------------------------------------------------")
    print()
    #username
    u_name=username(cn,dob,ac)
    #password(r_num,ac,cn,consumer,dob)
    v_password=password(r_num,ac,cn,u_name,dob)

    #SQL2
    COMD2='''INSERT INTO customers(ACCOUNT_NUMBER,CONSUMER_NO,NAME,DOB,FatherName,MotherName,Address,USER,PASS)
    Values({},{},'{}','{}','{}','{}','{}','{}','{}')'''.format(ac,cn,name,dob,fname,mname,address,u_name,v_password)
    cusr.execute(COMD2)

    #SQL3
    comd3='''CREATE TABLE IF NOT EXISTS transaction (NO INT auto_increment PRIMARY KEY,USER VARCHAR(45) NOT NULL,TYPE VARCHAR(10) NOT NULL,DOT VARCHAR(45) NOT NULL,
    AMOUNT BigInt NOT NULL,AVAILABLE_BAL BigInt NOT NULL,REMARK VARCHAR(255))'''
    cusr.execute(comd3)

    #SQL4
    com4='''INSERT INTO transaction(USER,TYPE,DOT,AMOUNT,AVAILABLE_BAL,REMARK)
    values('{}','{}','{}',{},{},'{}')'''.format(u_name,"CREDIT",str(t),1,1,"TEST")
    cusr.execute(com4)
    
    n=n+1 #user control
    
    ask=input("Enter 'Y' to Open ANOTHER New Account(if not then skip) :")
    print()
#SQL
cusr.execute("Select * from customers")
db_ck=cusr.fetchall()
#SQL
check_1=len(db_ck)
if(check_1!=0):
    cusr.execute("SELECT USER FROM customers")
    rdata=cusr.fetchall()
    for i in rdata:
        ruser=i[0]
        l_user.append(ruser)
    run_1=1
    while(run_1==1):
        run_1=0
        print()
        print("Welcome To CUI Banking Interface Of ",bankname)
        print()
        #login portal
        check_3=login(l_user)
        if(check_3[0]==1):
            cusr.execute("SELECT * FROM customers WHERE USER = '{}' ".format(check_3[1]))
            cusdata=cusr.fetchone()
            print("Loged in with Consumer No.",cusdata[1])
            print()
            #u_trans=[]
            passbook(bankname,cusdata[0],ifsc,cusdata[2],cusdata[1],cusdata[3],cusdata[4],cusdata[5],t,cusdata[6])
            
            run_2=1
            while(run_2==1):
                run_2=0
                
                ask_log=input("Enter 'D' to Deposit Money \n'S' to Send to Money \n'W' to Withdrawal Money \n'T' to view transactions \n'U' to Change Username \n'P' to Change Password \n'N' to Log Out\n::::")

                if(ask_log=="D" or ask_log=="d"):
                    #SQL
                    com5="SELECT * FROM transaction WHERE USER= '{}' ORDER BY NO DESC Limit 1".format(cusdata[7])
                    cusr.execute(com5)
                    dala=cusr.fetchone()
                    available_bal=dala[4]
                    
                    #SQL
                    cr_am=int(input("Enter the Amount : ₹"))
                    cr_remark=remark()

                    available_bal=available_bal+cr_am
                    print(cr_am,"sucessfully credited and Availble Balance is",available_bal)

                    #sql
                    com6='''INSERT INTO transaction (USER,TYPE,DOT,AMOUNT,AVAILABLE_BAL,REMARK)
                    values('{}','{}','{}',{},{},'{}')'''.format(cusdata[7],"CREDIT",t,cr_am,available_bal,cr_remark)
                    cusr.execute(com6)
                    #sql
                    
                    ask_log_1=input("Enter 'P' proceed to other task or Any Key to Log Out \n::::::")
                    if(ask_log_1=='p' or ask_log_1=="P"):
                        run_2=1
                    else:
                        run_1=0

                elif(ask_log=="S" or ask_log=="s"):
                    ask_ac=int(input("Enter the Beneficiary's Account No. :"))
                    ask_ifsc=input("Enter the Beneficiary's IFSC :")
                    ask_name=input("Enter the Beneficiary's Name :")
                    dr_am_sd=int(input("Enter the Amount : ₹"))
                    dr_sd_remark=remark()

                    #sql
                    com7="SELECT * FROM transaction WHERE USER = '{}' ORDER BY NO DESC Limit 1".format(cusdata[7])
                    cusr.execute(com7)
                    dala=cusr.fetchone()
                    available_bal=dala[4]
                    #sql
                    
                    available_bal=available_bal-dr_am_sd
                    print("Succesfully",dr_am_sd,"has been sent to",ask_name)
                    print("Available balance is : ₹",available_bal,sep="")

                    #sql
                    com8='''INSERT INTO transaction (USER,TYPE,DOT,AMOUNT,AVAILABLE_BAL,REMARK)
                    values('{}','{}','{}',{},{},'{}')'''.format(cusdata[7],"DEBIT",t,dr_am_sd,available_bal,dr_sd_remark)
                    cusr.execute(com8)
                    
                    ask_log_1=input("Enter 'P' proceed to other task or Any Key to Log Out \n::::::")
                    if(ask_log_1=='p' or ask_log_1=="P"):
                        run_2=1
                    else:
                        run_1=0

                elif(ask_log=="W" or ask_log=="w"):
                    print("WIthdrawal Not possible on this device")

                    ask_log_1=input("Enter 'P' proceed to other task or Any Key to Log Out \n::::::")
                    if(ask_log_1=='p' or ask_log_1=="P"):
                        run_2=1
                    else:
                        run_1=0

                elif(ask_log=="T" or ask_log=="t"):
                    transaction(cusdata[7])

                    ask_log_1=input("Enter 'P' proceed to other task or Any Key to Log Out \n::::::")
                    if(ask_log_1=='p' or ask_log_1=="P"):
                        run_2=1
                    else:
                        run_1=0

                elif(ask_log=="U" or ask_log=="u"):
                    change_username=username(cusdata[1],cusdata[3],cusdata[0])
                    
                elif(ask_log=="P" or ask_log=="p"):
                    password(r_num,cusdata[0],cusdata[1],cusdata[7],cusdata[3])

                elif(ask_log=="N" or ask_log=="n"):
                    print("Log Out Sucessfull for Consumer No.",cusdata[1])
                    run_1=1
        continue        
else:
    print("No Account Created")

q.close()

 








    
