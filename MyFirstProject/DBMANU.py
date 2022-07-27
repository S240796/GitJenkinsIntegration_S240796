import pymysql
db = None
cur = None
def connectDB():
    global db,cur
    db = pymysql.connect(host='localhost',
                     user='shubham',
                     password='',
                     database='python_3_10_2')
    cur = db.cursor()
    
    
def disconnectDB():
    db.close()
    cur.close()

def readallrecords():
    connectDB()
    query = 'select * from employees'
    cur.execute(query)
    result = cur.fetchall()
    for i in result:
        print(i)
    disconnectDB()

def searchrecord(i):
    connectDB()
    query = f'select * from employees where EMPLOYEE_ID = {i}'
    cur.execute(query)
    result = cur.fetchall()
    for i in result:
        print(i)
    disconnectDB()

def deleterecord():
    connectDB()
    i = int(input('Enter EMPLOYEE_ID to serch data :'))
    query = f'delete from employees where EMPLOYEE_ID = {i}'
    cur.execute(query)
    result = cur.fetchall()
    for i in result:
        print(i)
    db.commit()    
    disconnectDB()
    
def insertrecord():
    connectDB()
    EMPLOYEE_ID = int(input('Enter EMPLOYEE_ID:'))
    FIRST_NAME = (input('Enter FIRST_NAME:'))
    LAST_NAME = (input('Enter LAST_NAME:'))
    EMAIL = (input('Enter EMAIL:'))
    PHONE = (input('Enter PHONE:'))
    HIRE_DATE = (input('Enter HIRE_DATE:'))
    MANAGER_ID = int(input('Enter MANAGER_ID:'))
    JOB_TITLE = (input('Enter JOB_TITLE:'))
    query = f'Insert into EMPLOYEES(EMPLOYEE_ID,FIRST_NAME,LAST_NAME,EMAIL,PHONE,HIRE_DATE,MANAGER_ID,JOB_TITLE)values({EMPLOYEE_ID},"{FIRST_NAME}","{LAST_NAME}","{EMAIL}","{PHONE}",current_date(),{MANAGER_ID},"{JOB_TITLE}")'
    #print(query)
    cur.execute(query)
    db.commit()

def updatedata(CHOICE,EMPLOYEE_ID,FIRST_NAME):
    connectDB()
    if CHOICE==1:
        query = f'update EMPLOYEES set FIRST_NAME="{FIRST_NAME}" where EMPLOYEE_ID={EMPLOYEE_ID}'
    elif CHOICE==2:
        query = f'update EMPLOYEES set LAST_NAME="{FIRST_NAME}" where EMPLOYEE_ID={EMPLOYEE_ID}'
    elif CHOICE==3:
        query = f'update EMPLOYEES set EMAIL="{FIRST_NAME}" where EMPLOYEE_ID={EMPLOYEE_ID}'
    elif CHOICE==4:
        query = f'update EMPLOYEES set PHONE="{FIRST_NAME}" where EMPLOYEE_ID={EMPLOYEE_ID}'
    elif CHOICE==5:
        query = f'update EMPLOYEES set HIRE_DATE="{FIRST_NAME}" where EMPLOYEE_ID={EMPLOYEE_ID}'
    elif CHOICE==6:
        query = f'update EMPLOYEES set MANAGER_ID={FIRST_NAME} where EMPLOYEE_ID={EMPLOYEE_ID}'
    elif CHOICE==7:
        query = f'update EMPLOYEES set JOB_TITLE="{FIRST_NAME}" where EMPLOYEE_ID={EMPLOYEE_ID}'
    else:
        print('wrong choice')
    cur.execute(query)
    db.commit()
    disconnectDB()


    
while True:
    print('''select the operation you want to perform:
             1.Display all record
             2.Search record
             3.Insert new record
             4.Update Record
             5.Delete record
             0.Exit''')
    choice = int(input('Enter your choice: '))
    if choice==0:
        break
    elif choice==1:
          readallrecords()
    elif choice==2:
        i = int(input('Enter EMPLOYEE_ID to serch data :'))
        searchrecord(i)
    elif choice==3:
        insertrecord()
    elif choice==4:
        i = int(input('Enter ID to update data:'))
        print('Data before update')
        searchrecord(i)
        print('''select what you will have to update:
             1.FIRST_NAME
             2.LAST_NAME
             3.EMAIL
             4.PHONE
             5.HIRE_DATE
             6.MANAGER_ID
             7.JOB_TITLE
             0.Exit''')
        choice = int(input('Enter your choice: '))
        if choice==0:
            break
        elif choice==1:
            FIRST_NAME = (input('Enter FIRST_NAME:'))
        elif choice==2:
            FIRST_NAME = (input('Enter LAST_NAME:'))
        elif choice==3:
            FIRST_NAME = (input('Enter EMAIL:'))
        elif choice==4:
            FIRST_NAME = (input('Enter PHONE:'))
        elif choice==5:
            FIRST_NAME = (input('Enter HIRE_DATE:'))
        elif choice==6:
            FIRST_NAME = int(input('Enter MANAGER_ID:'))
        elif choice==7:
            FIRST_NAME = (input('Enter JOB_TITLE:'))

        updatedata(choice,i,FIRST_NAME)
        print('Data updated successfully')
        searchrecord(i)
    elif choice==5:
        deleterecord()
    
