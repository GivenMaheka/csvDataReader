# Shamiri Institute

## How it works

The python script should convert the MOCK_DATA.csv file into a Postgres table.

MOCK_DATA.csv is a csv file which has some missing data. The script should be able to handle the missing data and insert the data into the Postgres table.

The script should be able to run on any machine and should not require any manual intervention to run.

### Steps

1. Create a Postgres database

A/ CREATE DATABASE shamiti_users;

2. Create a table in the database using the csv file as a reference for the table structure

A/CREATE TYPE gender AS ENUM('Male','Female','Bigender');
A/ CREATE TABLE users(id BIGSERIAL NULL, first_name VARCHAR(20) NOT NULL, last_name VARCHAR(20) NULL, email VARCHAR(100) NOT NULL, gender gender NOT NULL, ip_address VARCHAR(50) NULL, isadmin BOOL NULL);

3. Clean the data and insert the data from the csv file into the postgres table
4. Update .env file with the connection details for the database (Note: You can use a local connection or a remote connection * if you are using a remote connection, please provide the connection details in the readme file)
5. Update requirements.txt file with the dependencies for the project
6. How would you improve the script to make it more efficient? (Note: You are not required to implement the improvements but list them in the readme file)

A/
To make the script run more efficient, I would segregate some code, for instance create a database file that will manage the connection and can be called in other files.
Having functions created to be triggered only on a specific event insted of having the program running some code that are not yet needed.


7. How you you ensure the script is running whenever the csv file is updated? (Note: You are not required to implement the improvements but list them in the readme file)

A/
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

filePath = '' # Path to the CSV file to be observed

class Handler(FileSystemEventHandler):
    def on_modified(self,event):
        if event.src_path == filePath:
            # Pass code to insert the new data.

observer = Observer()
observer.schedule(Handler(),".",recursive=True) # the local directory
observer.start()

try:
    while observer.is_alive():
        observer.join(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()


With the code above we start by calling for two important librarie, the Watchdog Observer and Event. These two are helpful tools that help us track any change within a folder or file.

We specify the path to the desired file that we wanna keep eyes on, the we create a Handler that we be checking the event and modifies the Database.
After assigning the observer, we schedule the event by passing the handler and the path to the directory we are observing, then we start the observation.
The try statement keeps an eye on whatever going on within or with the target and execute the Handler. In case of interruption the observation stops running.

8. Upload the final project to github and provide the link to the repository


### Language to run script
   ``Python 3 + ``


### Deployment Notes
Once you have created a Postgres database, please update the requirements.txt file with the dependencies for the project.

You will upload the final project to github and provide the link to the repository.

#### Good luck!