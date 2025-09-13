
## Create the one Python Script
## install the required db module
## pip install pymysql


#Step1: import the  required db module
import  pymysql

#Step2: Creating the Connection object using pymysql module

connecton_object = pymysql.connect(
    user='root',
    password='root',
    host='localhost'
)

#Step3: Creating the Cursor object using cursor() method  of connecton_object

cursor_object = connecton_object.cursor()


#Step4: Creating required SQL Query
sql = "show databases;"

#Step5: Execute the required SQl Query using execute() method of cursor_object

count = cursor_object.execute(sql)
print("Total",count,"Databases available")

#Step6:  Accessing required data from cursor_object using for-loop
'''
for tuple_db  in cursor_object: # (('db1',),('db2',),('db3',),....)
    print(tuple_db)
'''

'''
for tuple_db  in cursor_object:
    for db in tuple_db:
        print(db)
'''

#Step6:  Accessing required data from cursor_object using fetching methods

# using fetchall()
'''
data = cursor_object.fetchall() # (('db1',),('db2',),('db3',),....)
print(data)
'''

# using fetchmany()
'''
data = cursor_object.fetchmany() # (('db1',))
print(data)
'''

# using fetchmany(2)
'''
data = cursor_object.fetchmany(2) # (('db1',),('db2',))
print(data)
'''

# using fetchone()

data = cursor_object.fetchone() # ('db1',)
print(data)


#Step7: Close the all resources objects
cursor_object.close()
connecton_object.close()
print('Objects closed successfully!')


    
    
