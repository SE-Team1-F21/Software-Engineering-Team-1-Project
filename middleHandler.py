import psycopg2
import requests
import sys

#TODO: fetching data from database and pass to flask
#focusing on id and codename

#Fetching credentials with json
url_credentials = ''

data = requests.get(url_credentials).json()

credentials_list = []
user = ''
password = ''
host = ''
port = ''
database = ''

for i in range(len(data['values'])):
    credentials_list = data['values'][i]

user = credentials_list[0]
password = credentials_list[1]
host = credentials_list[2]
port = credentials_list[3]
database = credentials_list[4]

def connection(id, codeName):
    
    print("This data is from middleHanlder.py!")
    print("Inserting {0} to database...".format((id, codeName)))

    try:
        connection = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )
        
        cursor = connection.cursor()
        
        ###inserting id and name for now
        insert_query = """INSERT INTO player (id, codeName) VALUES (%s, %s)"""
        # test_to_insert = (7, 'test_user1')
        test_to_insert = (id, codeName)
        cursor.execute(insert_query, test_to_insert)
        connection.commit()
        print("Inserted this data successfully")
        
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert this data")

    finally:
        #closing database connection
        if connection:
            cursor.close()
            connection.close()
            print("Disconnecting database...")
            