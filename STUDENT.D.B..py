import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass
import sys
conn=mysql.connector.connect(user="root",database="studentadmission")
cursor=conn.cursor()
print('Connected To Database')
class User:  
    def EnquiryStudents(self,ename,econtact,ecourse,eemail):
        query="insert into Students(name,contactno,course,emailid) values('"+ename+"',"+str(econtact)+",'"+ecourse+"','"+eemail+"')"
        cursor.execute(query)
        conn.commit()
        print('Enquiry Added Successfully')
    def ShowEnquiryStudents(self):
        query="Select * from Students"
        cursor.execute(query)
        print("{:<5}{:<10}{:<10}{:<10}{:<25}{:<10}{:<5}".format('ID','Name','ContactNo','Course','Email-id','Status','Fees'))
        for s in cursor:
            print('{:<5}{:<10}{:<10}{:<10}{:<25}{:<10}{:<5}'.format(s[0],s[1],s[2],s[3],s[4],s[5],s[6]))  
    def ShowStudent(self):
        query="Select * from admission"
        cursor.execute(query)
        print("{:<5}{:<10}{:<10}{:<10}{:<25}{:<10}{:<5}".format('ID','Name','Contactno','Course','Emailid','Status','Fees'))
        for s in cursor:
            print('{:<5}{:<10}{:<10}{:<10}{:<25}{:<10}{:<5}'.format(s[0],s[1],s[2],s[3],s[4],s[5],s[6]))
    def DeleteStudentID(self,ID):
        query="delete from Students where id="+str(ID)
        cursor.execute(query)
        conn.commit()
        print('Record Deleted')
    def DeleteStudentByID(self,ID):
        query="delete from admission where id="+str(ID)
        cursor.execute(query)
        conn.commit()
        print('Record Deleted')
    def UpdateStudentName(self,ID,name):
         query="Update admission set name='"+name+"' where id="+str(ID)
         cursor.execute(query)
         conn.commit()
         print("Name Updated")
    def UpdateStudentCourse(self,ID,course):
         query="Update admission set course='"+course+"' where id="+str(ID)
         cursor.execute(query)
         conn.commit()
         print("Course Updated")
    def ChangeStatus(self,ID,status):
         query="Update admission set status='"+status+"' where id="+str(ID)
         cursor.execute(query)
         conn.commit()
         print("Status Updated")
    def SearchStudentByID(self,ID):
         m='ID Not Found'
         query="Select * from admission where id="+str(ID)
         cursor.execute(query)
         print("{:<5}{:<15}{:<15}{:<10}{:<15}{:<10}".format('ID','Name','Contactno','Course','Emailid','Fees'))
         for s in cursor:            
                  print('{:<5}{:<15}{:<15}{:<10}{:<15}{:<10}'.format(s[0],s[1],s[2],s[3],s[4],s[5]))
                  m='ID Found'
         print(m)
    def SearchStudentByName(self,name):
         m='Name Not Found'
         query="Select * from admission where name='"+name+"'"
         cursor.execute(query)
         print("{:<5}{:<15}{:<15}{:<10}{:<15}{:<10}".format('ID','Name','Contactno','Course','Emailid','Fees'))
         for s in cursor:            
                  print('{:<5}{:<15}{:<15}{:<10}{:<15}{:<10}'.format(s[0],s[1],s[2],s[3],s[4],s[5]))
                  m='ID Found'
         print(m)
    def SearchStudentByCourse(self,course):
         m='Course Not Found'
         query="Select * from admission where course='"+course+"'"
         cursor.execute(query)
         print("{:<5}{:<15}{:<15}{:<10}{:<15}{:<10}".format('ID','Name','Contactno','Course','Emailid','Fees'))
         for s in cursor:            
                  print('{:<5}{:<15}{:<15}{:<10}{:<15}{:<10}'.format(s[0],s[1],s[2],s[3],s[4],s[5]))
                  m='Course Found'                 
         print(m)    
    
def StudentEnquiry():
    while(True):
        try:
            print("1:Enquiry.\t2:Admission.\t3:Student Details.")
            u=User()
            c=int(input('Enter Choice:'))
            if(c==0):
                break
            elif(c==1):
                print("1:AddEnquiry.\t2:ShowEnquiry.\t3:DeleteEnquiryID")   
                c=int(input('Enter Choice:'))
                if(c==1):
                 ename= input('Name:')
                 econtact=int(input('Contact-No:'))
                 ecourse=input('Course:')
                 eemail=input('Email-id:')
                 u.EnquiryStudents(ename,econtact,ecourse,eemail)
                elif(c==2):
                 u.ShowEnquiryStudents()
                elif(c==3):
                  ID=int(input('Enter-ID:'))
                  u.DeleteStudentID(ID)
            elif(c==2):
             print("1:AddStudent.\t2:ShowStudents.")
             c=int(input('Enter Choice:'))
             if(c==1):   
              id=int(input('Enquiry ID:'))
              query="Select name,contactno,course,emailid,fees from Students where id="+str(id)
              cursor.execute(query)
              m='ID Not Found'        
              print("{:<5}{:<15}{:<15}{:<20}{:<10}".format('Name','Contactno','Course','Emailid','Fees'))
              for s in cursor:
                ename=s[0]
                econtact=s[1]
                ecourse=s[2]
                eemail=s[3]
                fees=s[4]
                print('{:<5}{:<15}{:<15}{:<20}{:<10}'.format(s[0],s[1],s[2],s[3],s[4]))
                m='---------'
                print(m)
                print('1:Confirm.2.Cancel.')
                c=int(input('Choice:'))
                if(c==1):        
                    query="insert into Admission(name,contactno,course,emailid,fees) values('"+ename+"',"+str(econtact)+",'"+ecourse+"','"+eemail+"',"+str(fees)+")"
                    cursor.execute(query);
                    conn.commit();
                    print('Admission Done')
                    SendMail(eemail,'Congratulations!Your Admission is Confirm')    
                else:
                    print('Thank You')             
             elif(c==2):
              u.ShowStudent()
            elif(c==3):
             print("1:UpdateStudent.\t2:DeleteStudentByID.\t3:SearchStudent")
             c=int(input('Enter Choice:'))
             if(c==1):
              print("1:Name.\t2:Course.\t3:ChangeStatus")
              c=int(input('Enter Choice:'))
              if(c==1):
                i=int(input('Enter-ID:'))
                n=input('Enter-Name:')
                u.UpdateStudentName(i,n)
              elif(c==2):
                i=int(input('Enter-ID:'))
                n=input('Enter-Course:')
                u.UpdateStudentCourse(i,n)
              elif(c==3):
                 id=int(input('Enter-ID:'))
                 status=input('Enter Status:')
                 u.ChangeStatus(id,status)  
             elif(c==2):
                ID=int(input('Enter-ID:'))
                u.DeleteStudentByID(ID)
             elif(c==3):
                print("1:ID.\t2:Name.\t3:Course.")
                c=int(input('Enter Choice:'))
                if(c==1):
                  i=int(input('Enter-ID:'))
                  u.SearchStudentByID(i)
                elif(c==2):
                  n=input('Enter-Name:')
                  u.SearchStudentByName(n)
                elif(c==3):
                  c=input('Enter-Course:')
                  u.SearchStudentByCourse(c)
        except mysql.connector.errors.IntegrityError as e:
            print(e)
    print('Good Bye!')       

def SendMail(to,message):
    #create message object instance
    msg = MIMEMultipart()
    # setup the parameters of the message
    #password = input("enter password :")
    #password=getpass.getpass('Enter password ',"")
    #password = raw_input("Enter Password: ")
    password="Aptech@123"
    msg['From'] = "roojay0000@gmail.com"
    msg['To'] = to
    msg['Subject'] = "Admission Confirmation"
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'],msg.as_string())
    server.quit()
    print ("successfully sent email to %s:" % (msg['To']))


    
                

    
    
    
