import mysql.connector as sql
import os
conn=sql.connect(host='localhost',user='root',password='root',database='ATM_MACHINE')
c1=conn.cursor()



def clear():
      os.system('cls')



def auto(ph):
      c1.execute(f'''SELECT ACCONT_NO FROM records WHERE PHONE_NO="{ph}";''')
      x=c1.fetchone()
      x=x[0]
      return x



def atm_logo():
            print("================================================================================")
            print(r'''                          /$$$$$$  /$$$$$$$$ /$$      /$$
                         /$$__  $$|__  $$__/| $$$    /$$$
                        | $$  | $$   | $$   | $$$$  /$$$$
                        | $$$$$$$$   | $$   | $$ $$/$$ $$
                        | $$__  $$   | $$   | $$  $$$| $$
                        | $$  | $$   | $$   | $$\  $ | $$
                        | $$  | $$   | $$   | $$ \/  | $$
                        |__/  |__/   |__/   |__/     |__/                                     ''')
            print("================================================================================")



def cre_acc():
      print("================================================================================")
      print(r'''       ___ ___ ___   _ _____ ___     _   ___ ___ ___  _   _ _  _ _____ 
      / __| _ \ __| /_\_   _| __|   /_\ / __/ __/ _ \| | | | \| |_   _|
     | (__|   / _| / _ \| | | _|   / _ \ (_| (_| (_) | |_| | .` | | |  
      \___|_|_\___/_/ \_\_| |___| /_/ \_\___\___\___/ \___/|_|\_| |_|  
                                                                   ''')
      print("================================================================================")



def login_logo():
      print("================================================================================")
      print(r'''                          _     ___   ____ ___ _   _ 
                         | |   / _ \ / ___|_ _| \ | |
                         | |  | | | | |  _ | ||  \| |
                         | |__| |_| | |_| || || |\  |
                         |_____\___/ \____|___|_| \_|
                             ''')
      print("================================================================================")



def welcome_logo():
      print("================================================================================")

      print(r'''             _    _ _____ _     _____ ________  ___ _____ _ 
            | |  | |  ___| |   /  __ \  _  |  \/  ||  ___| |
            | |  | | |__ | |   | /  \/ | | | .  . || |__ | |
            | |/\| |  __|| |   | |   | | | | |\/| ||  __|| |
            \  /\  / |___| |___| \__/\ \_/ / |  | || |___|_|
             \/  \/\____/\_____/\____/\___/\_|  |_/\____/(_)
            ''')
      print("================================================================================")



def deposit_logo():
      print("================================================================================")
      print(r'''      8888888b.  8888888888 8888888b.   .d88888b.   .d8888b. 8888888 88888888888 
      888  "Y88b 888        888   Y88b d88P" "Y88b d88P  Y88b  888       888     
      888    888 888        888    888 888     888 Y88b.       888       888     
      888    888 8888888    888   d88P 888     888  "Y888b.    888       888     
      888    888 888        8888888P"  888     888     "Y88b.  888       888     
      888    888 888        888        888     888       "888  888       888     
      888  .d88P 888        888        Y88b. .d88P Y88b  d88P  888       888     
      8888888P"  8888888888 888         "Y88888P"   "Y8888P" 8888888     888     
                                    ''')
      print("================================================================================")



def withdrawal_logo():
      print("================================================================================")
      print(r'''       _    _ _____ _____ _   _____________  ___  _    _  ___   _     
      | |  | |_   _|_   _| | | |  _  \ ___ \/ _ \| |  | |/ _ \ | |    
      | |  | | | |   | | | |_| | | | | |_/ / /_\ \ |  | / /_\ \| |    
      | |/\| | | |   | | |  _  | | | |    /|  _  | |/\| |  _  || |    
      \  /\  /_| |_  | | | | | | |/ /| |\ \| | | \  /\  / | | || |____
       \/  \/ \___/  \_/ \_| |_/___/ \_| \_\_| |_/\/  \/\_| |_/\_____/
            ''')
      print("================================================================================")


def transfer_logo():
      print("================================================================================")
      print(r'''__________ __________        _     ___      ___  ____  ________ __________ ________    
MMMMMMMMMM `MMMMMMMMM       dM.    `MM\     `M' 6MMMMb\`MMMMMMM `MMMMMMMMM `MMMMMMMb.  
/   MM   \  MM      \      ,MMb     MMM\     M 6M'    ` MM    \  MM      \  MM    `Mb  
    MM      MM             d'YM.    M\MM\    M MM       MM       MM         MM     MM  
    MM      MM    ,       ,P `Mb    M \MM\   M YM.      MM   ,   MM    ,    MM     MM  
    MM      MMMMMMM       d'  YM.   M  \MM\  M  YMMMMb  MMMMMM   MMMMMMM    MM    .M9  
    MM      MM    `      ,P   `Mb   M   \MM\ M      `Mb MM   `   MM    `    MMMMMMM9'  
    MM      MM           d'    YM.  M    \MM\M       MM MM       MM         MM  \M\    
    MM      MM          ,MMMMMMMMb  M     \MMM       MM MM       MM         MM   \M\   
    MM      MM      /   d'      YM. M      \MM L    ,M9 MM       MM      /  MM    \M\  
   _MM_    _MMMMMMMMM _dM_     _dMM_M_      \M MYMMMM9 _MM_     _MMMMMMMMM _MM_    \M\_                                                                                       
''')
      print("================================================================================")



def balance_logo():
      print("================================================================================")
      print(r'''       /$$$$$$$   /$$$$$$  /$$        /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$$
      | $$__  $$ /$$__  $$| $$       /$$__  $$| $$$ | $$ /$$__  $$| $$_____/
      | $$  \ $$| $$  \ $$| $$      | $$  \ $$| $$$$| $$| $$  \__/| $$      
      | $$$$$$$ | $$$$$$$$| $$      | $$$$$$$$| $$ $$ $$| $$      | $$$$$   
      | $$__  $$| $$__  $$| $$      | $$__  $$| $$  $$$$| $$      | $$__/   
      | $$  \ $$| $$  | $$| $$      | $$  | $$| $$\  $$$| $$    $$| $$      
      | $$$$$$$/| $$  | $$| $$$$$$$$| $$  | $$| $$ \  $$|  $$$$$$/| $$$$$$$$
      |_______/ |__/  |__/|________/|__/  |__/|__/  \__/ \______/ |________/
            ''')
      print("================================================================================")



def closeaccount_logo():
      print("================================================================================")
      print(r'''    ____ _     ___  ____  _____      _    ____ ____ ___  _   _ _   _ _____ 
   / ___| |   / _ \/ ___|| ____|    / \  / ___/ ___/ _ \| | | | \ | |_   _|
  | |   | |  | | | \___ \|  _|     / _ \| |  | |  | | | | | | |  \| | | |  
  | |___| |__| |_| |___) | |___   / ___ \ |__| |__| |_| | |_| | |\  | | |  
   \____|_____\___/|____/|_____| /_/   \_\____\____\___/ \___/|_| \_| |_|  
            ''')
      print("================================================================================")



def create_account():
      c="y"
      while c=="y":
            cre_acc()
            name=input("Enter your name: ")
            while True:
                  passw=int(input("Enter your PIN: "))
                  if len(str(passw))==4:
                        break
                  else:
                        print("PIN must be only 4 Digit long!")
                        print(' ')
                        continue
            while True:
                  ph=int(input("Enter phone number: "))
                  if len(str(ph))==10:
                        break
                  else:
                        print("Phone Number must be only 10 Digit long!")
                        print(' ')
                        continue
            
            ab="insert into records(PASSWORD,NAME,PHONE_NO) values({},'{}',{})".format(passw,name,ph)
            clear()
            c1.execute(ab)
            conn.commit()
            cre_acc()
            print("Account successfully created")
            print('your account number is '+'\033[1m'+str(auto(ph))+'\033[0m')

            while True:
                  print(' ')
                  print("The minimum balance is 1000 ")
                  s=int(input("Enter the money to be deposited :"))
                  if s>=1000:
                        x=auto(ph)
                        sr="update records set  CR_AMT={} where ACCONT_NO={}".format(s,x)
                        c1.execute(sr)
                        conn.commit()
                        ef="update records set balance=cr_amt-withdrawl where ACCONT_NO={}".format(x)
                        c1.execute(ef)
                        conn.commit()
                        clear()
                        print("sucessfully deposited")
                        input('Press enter to continue')
                        clear()
                        break
                  else:
                        clear()
                        cre_acc()
                        print("Amount less than 1000.")
                        input('Press Enter to Continue')
                        clear()
                        cre_acc()
                        continue
            break



def login():
      y="y"
      while y=="y":
            login_logo()
            print(' ')
            acct=int(input("Enter your account number:"))
            cb="select * from records where ACCONT_NO={}".format(acct)
            c1.execute(cb)
            c1.fetchall()
            data=c1.rowcount

            if data==0:
                  print("your Account does not exists")
                  input("Press Enter to Continue")
                  clear()
            else:
                  for i in range(3):
                        pas=int(input("Enter your password  :"))

                        e="select password from records where ACCONT_NO={}".format(acct)
                        c1.execute(e)
                        a=c1.fetchone()
                        d=list(a)

                        if pas!=d[0]:
                              print("Wrong PIN, Try Again!")
                              continue
                        elif pas==d[0]:
                              break
                  else:
                        clear()
                        print("Too many Incorrect Attempts!")
                        input("Press Enter to Continue")
                        clear()
                        break
                  
                  clear()
                  welcome_logo()
                  print(' ')
                  print("                                 Welcome Back!")
                  print(" ")
                  print("1. Depositng money")
                  print("2. withdrawing money")
                  print("3. Transfering money")
                  print("4. Checking balance")
                  print("5. Exit")
                  print(' ')
                  r=int(input("(1/2/3/4/5): "))

                  if r==1:
                        clear()
                        deposit_logo()
                        amt=int(input("Enter the money to be deposited:"))

                        sr="update records set CR_AMT=CR_AMT + {} where ACCONT_NO={}".format(amt,acct)
                        c1.execute(sr)
                        conn.commit()
                        ef="update records set balance=cr_amt-withdrawl where ACCONT_NO={}".format(acct)
                        c1.execute(ef)
                        conn.commit()
                        clear()
                        print("sucessfully deposited")
                        input("Press Enter to Continue")
                        clear()
                        break
                  
                  if r==2:
                        clear()
                        withdrawal_logo()
                        amt=int(input("Enter the money to withdraw:"))
                        
                        ah="select  BALANCE from records where accont_no={}".format(acct)
                        c1.execute(ah)
                        m=c1.fetchone()
                        if amt >m[0]:
                              print("Your are having less than",amt)
                              input("Press Enter To Continue")
                              clear()
                              break

                        else:
                              sr="update records set balance=balance - {}  where ACCONT_NO={}".format(amt,acct)
                              ed="update records set  WITHDRAWL ={}  where ACCONT_NO={}".format(amt,acct)
                              c1.execute(ed)
                              c1.execute(sr)
                              conn.commit()
                              clear()
                              print("Sucessfully updatad!")
                              input("Press Enter to Continue")
                              clear()
                              break
                  
                  if r==3:
                        clear()
                        transfer_logo()
                        act=int(input("Enter the accont number to be transferrsd :"))

                        cb="select * from records where ACCONT_NO={}".format(act)
                        c1.execute(cb)
                        c1.fetchall()
                        data=c1.rowcount

                        if data==0:
                              print('The account does not exist:')
                              input("Press Enter to Continue")
                              clear()
                        elif data==1:
                              clear()
                              transfer_logo()
                              print(act ,"number exists")
                              m=int(input("Enter the money to be transferred :"))

                              ah="select  BALANCE from records where accont_no={}".format(acct)
                              c1.execute(ah)
                              c=c1.fetchone()
                              if m > c[0]:
                                    clear()
                                    print("Your are having less than",m)
                                    input("Press Enter To Continue")
                                    clear()
                                    break
                                   
                              else:
                                    av="update records set balance=balance-{} where ACCONT_NO={}".format(m,acct)  
                                    cv="update records set balance=balance+{} where ACCONT_NO={}".format(m,act)
                                    w="update records set withdrawl=withdrawl+{} where accont_no={}".format(m,acct)
                                    t="update records set  CR_AMT=CR_AMT+{} where accont_no={}".format(m,act)
                                    c1.execute(av)
                                    c1.execute(cv)
                                    c1.execute(w)
                                    c1.execute(t)
                                    conn.commit()
                                    
                                    clear()
                                    print("Sucessfully transfered")
                                    input('Press Enter to Continue')
                                    clear()
                                    break

                  elif r==4:
                        clear()
                        balance_logo()
                        ma="select balance from records where accont_no={}".format(acct)
                        c1.execute(ma)
                        k=c1.fetchone()
                        print("Balance in your account=",k[0])
                        input("Press Enter to Continue")
                        clear()
                        break
                  
                  elif r==5:
                        clear()
                        break

                  else:
                        print("Invalid Choice!")
                        input("Press Enter to Continue")
                        continue
                    


def close_account():
      y="y"
      while y=="y":
            closeaccount_logo()
            print(' ')
            acct=int(input("Enter your account number:"))
            cb="select * from records where ACCONT_NO={}".format(acct)
            c1.execute(cb)
            c1.fetchall()
            data=c1.rowcount

            if data==0:
                  print("your Account does not exists")
                  input("Press Enter to Continue")
                  clear()
            else:
                  for i in range(3):
                        pas=int(input("Enter your PIN  :"))

                        e="select password from records where ACCONT_NO={}".format(acct)
                        c1.execute(e)
                        a=c1.fetchone()
                        d=list(a)

                        if pas!=d[0]:
                              print("Wrong PIN, Try Again!")
                              continue
                        elif pas==d[0]:
                              break
                  else:
                        clear()
                        print("Too many Incorrect Attempts!")
                        input("Press Enter to Continue")
                        clear()
                        break

                  clear()
                  closeaccount_logo()
                  print('are you sure you want to clos this account?')
                  ans=input('y/n: ')
                  if ans=='y':
                        c1.execute(f'delete from records where ACCONT_NO={acct}')
                        conn.commit()
                        clear()
                        closeaccount_logo()
                        print('Account is now Closed!')
                        input("Press Enter to Continue")
                        clear()
                        break
                  
                  else:
                        closeaccount_logo()
                        print('Account Termination Cancelled!')
                        input("Press Enter to Continue")
                        clear()
                        break



while True:
      atm_logo()
      print('''
                                    WELCOME
      what would you like to do?
            ''')
      print("1.Create account")
      print("2.Login to account")
      print("3.Close account")
      print("4.Exit")

      op=int(input("(1/2/3/4): "))

      clear()
      if op==1:
            create_account()
      
      elif op==2:
            login()

      elif op==3:
            close_account()
      
      elif op==4:
            print("Exiting")
            clear()
            print(r'''      __     _____ ____ ___ _____      _    ____    _    ___ _   _ _ 
      \ \   / /_ _/ ___|_ _|_   _|    / \  / ___|  / \  |_ _| \ | | |
       \ \ / / | |\___ \| |  | |     / _ \| |  _  / _ \  | ||  \| | |
        \ V /  | | ___) | |  | |    / ___ \ |_| |/ ___ \ | || |\  |_|
         \_/  |___|____/___| |_|   /_/   \_\____/_/   \_\___|_| \_(_)
                                                                  ''')
            print(' ')
            input("Press Enter to Exit")
            c1.close()
            break

      else:
            print("Invalid Choice!")
            input('Press Enter to Continue')
            clear()
