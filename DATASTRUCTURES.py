import random
import smtplib
import json
import time
Id=[]
info={}
bus1=[]
tktlst=[]
print(' WELCOME TO   GROUP 3  TICKET BOOKING SYSTEM')               

lst=list()
for i in range(1,51):
    lst.append(i)
fname=list()
for j in range(1,51):
    fname.append(j)
fname=list()
for j in range(1,51):
    fname.append(j)
lname=list()
for k in range(1,51):
    lname.append(k)
agep=list()
for i in range(1,51):
    agep.append(i)
Departures=list()
for i in range(1,51):
    Departures.append(i)
Destinatione=list()
for i in range(1,51):
    Destinatione.append(i)
Unique=list()
for o in range(1,51):
    Unique.append(o)
mailid=list()
for g in range(1,51):
    mailid.append(g)
r=1

while r !=0:
    
    print("1.Book ticket ")
    print("2.Check Tickt Status ")
    print('3.Cancel ticket')
    print("4.Check detail of booked ticket ")
    
    choice = int(input("\nEnter your option : "))

    
    if choice==1:
        tic=int(input('Enter seat no '))
        if lst[tic-1]==tic:
            fname1=str(input('Enter your  first name \n'))
            lname1=str(input('Enter your last name \n'))
            age1=int(input('Enter your age \n'))
            Departure =str(input('Enter your station of Departure \n'))
            Destination=str(input('Enter your station of Destination \n'))
            mail=input('Enter your gmail id \n')
            bus1.append(mail)
            lst.pop(tic-1)
            lst.insert(tic-1,'B')
            fname.pop(tic-1)
            lname.pop(tic-1)
            agep.pop(tic-1)
            Departures.pop(tic-1)
            Destinatione.pop(tic-1)
            mailid.pop(tic-1)
            fname.insert(tic-1,fname1)
            lname.insert(tic-1,lname1)
            agep.insert(tic-1,age1)
            Departures.insert(tic-1,Departure)
            Destinatione.insert(tic-1,Destination)
            mailid.insert(tic-1,mail)
            a=random.randint(1000000,100000000)
            if a in Id:
                b=random.randint(1000000,100000000)
                Unique.insert(tic-1,b)
                Id.append(Unique)
            elif a not in Id:
                Unique.insert(tic-1,a)
                Id.append(Unique)
            text='YOUR TICKET IS BOOKED'+'\n'+str(fname1)+' '+str(lname1)+'\n'+str(age1)+'\n'+str(tic)+'\n'+str(Destination)+'\n'+str(Departure)+'\n'+'BUS DEPARTURE TIMINGS: 2P.M'+'\n'+'BUS ARRIVAL TIMINGS: 8P.M'
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("group3pts@gmail.com", "Pts@1234")
            server.sendmail("group3pts@gmail.com",mail,text)
            server.quit()
            print('Sent sucessfully')
                    
            print('\n*************************')
            print("your Ticket is booked")
            print('*************************\n')
            print('!!!!!Done!!!!!')
                    
        else:
            print('\n*************************')
            print('seat is already booked try other seat')
            print('*************************\n')

            
            
    elif choice==2:
        dest=str(input('Enter your destination : '))
        for k in lst:
            print(k,end=" ")
        print('\n')
    



           
    elif choice==3:
        tic=int(input('Enter seat no '))
        
        mail=input('Please Enter Your mail id \n')
        if mail in bus1:
            bus1.remove(mail)
            if (lst[tic-1]==tic):
                print('\n*************************')
                print("This seat is not Booked")
                print('*************************\n')
            elif lst[tic-1]!=tic:
                lst.pop(tic-1)
                lst.insert(tic-1,tic)
                fname.pop(tic-1)
                fname.insert(tic-1,tic)
                lname.pop(tic-1)
                lname.insert(tic-1,tic)
                agep.pop(tic-1)
                agep.insert(tic-1,tic)
                Departures.pop(tic-1)
                Departures.insert(tic-1,tic)
                Destinatione.pop(tic-1)
                Destinatione.insert(tic-1,tic)
                mailid.pop(tic-1)
                mailid.insert(tic-1,tic)
                text='!!!!!!!!!!Your Ticket Is Cancelled!!!!!!!!!!'
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server.login("group3pts@gmail.com", "Pts@1234")
                server.sendmail("group3pts@gmail.com",mail,text)
                server.quit()
                print('Sent sucessfully')
                print('\n*************************')
                print('your ticket is canceled')
                print('*************************\n')
            

                
            
    elif choice==4:
        s=int(input('Enter seat no \n'))
        s=s-1
        if fname[s]==s+1:
            print('\n*********')
            print('this seat is not booked')
            print('*********\n')
        else:
            print('\n*********')
            print('Customer Name is :',fname[s].title(),'',lname[s].title())
            print('Age is : ',agep[s] )
            print('DEPARTURE: ',Departures[s].title() )
            print('DESTINATION : ',Destinatione[s].title() )
            print('CUSTOMER ID: ',Unique[s] )
            print('*********\n')
            
            
    elif choice==54321:
        r=0
        break

        
    else:
        print('\n*************************')
        print('you are enter wrong key\n')
        print('*************************\n')

    
for index in range(len(lname)):
    info[lname[index]]=[]
    info[lname[index]].append(agep[index])
    info[lname[index]].append(Departures[index])
    info[lname[index]].append(Destinatione[index])
    info[lname[index]].append(Unique[index])
    info[lname[index]].append(lst[index])
    info[lname[index]].append(mailid[index])
w=list(info.keys())
for h in range(len(w)):
    if(type(w[h])!=str):
        del info[w[h]]


    
with open('pass_details.json', 'w') as fp:
    json.dump(info, fp, indent=4)
print('File sucessfully created')
print('Bus 1 information is available in 10 sec')
time.sleep(10)
if(len(bus1)>0):
    print('BUS 1 IS GOING TO START IN 10 SEC\n')
    time.sleep(10)
    print('BUS1 HAS STARTED\n')
    time.sleep(10)
    print('BUS1 REACHING ITS DESTINATION IN 10MINS')
    time.sleep(10)
    print('SENDING MAILS TO THE PASSENGERS IN BUS1')
    for i in bus1:
        text='YOU ARE ABOUT TO REACH YOUR DESTINATION IN 10 MINS....PLEASE BE READY!!!!'
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("group3pts@gmail.com", "Pts@1234")
        server.sendmail("group3pts@gmail.com",i,text)
        server.quit()
    time.sleep(10)
    print('SENDING THANK YOU MESSAGES')
    for i in bus1:
        text='YOU HAVE REACHED THE DESTINATION....THANK YOU FOR TRAVELLING WITH US \n Best wishes \n PTS Groups'
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("group3pts@gmail.com", "Pts@1234")
        server.sendmail("group3pts@gmail.com",i,text)
        server.quit()
else:
    print('NO PEOPLE IN BUS 1...!!!!!')
    
