
import pandas as pd
import psycopg2 as psql
import os 
from dotenv.main import load_dotenv

load_dotenv()

#connection to the Database
#We are fetching connection value from the .env file, for security purpose
con = psql.connect(
    host= os.environ['DB_HOST'],
    database= os.environ['DB_NAME'],
    password= os.environ['DB_PASSWORD'],
    port= os.environ['DB_PORT'],
)
cursor = con.cursor()




df = pd.read_csv('MOCK_DATA.csv') # Fetching data from the CSV file
df = df.fillna('') # Replacing the NaN value with empty space

for index,row in df.iterrows():
    
    # id = 0 if math.isnan(row['id']) else int(math.ceil(row['id'])) # ID as primary Key and auto increment in this case are not suppose to be empty. The database handle the value on its own
    fname = row['first_name']
    lname = row['last_name']
    email = row['email']
    gender = row['gender'] if row['gender'] != '' else 'UNKNOWN'
    ip = row['ip_address']
    isAdmin = row['isAdmin'] if row['isAdmin'] != '' else False #When an admin is not specify it register the default value which is false
    
    columns = "INSERT INTO users(first_name, last_name, email, gender, ip_address, isadmin) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (fname,lname,email,gender,ip,isAdmin)

    cursor.execute(columns,values) #execute the insert for each row in the csv file

count = cursor.rowcount #get the number of data inserted for debug purpose
print(count,'Inserted Successfully')

cursor.close()
con.commit()
con.close()


