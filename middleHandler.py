import psycopg2
import sys

#TODO: fetching data from database and pass to flask
#focusing on id and codename

#receive input argument
user = sys.argv[1]
password = sys.argv[2]
host = sys.argv[3]
port = sys.argv[4]
database = sys.argv[5]

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
    test_to_insert = (7, 'test_user1')
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