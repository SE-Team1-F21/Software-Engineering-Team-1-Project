import psycopg2

#TODO: fetching data from database and pass to flask

user = 'leemdipikfjyvk'
password = 'b02a82e4e956bd6b2308b373258f48e20d291ac795fbea568105ef238cd5a324'
host = 'ec2-23-22-191-232.compute-1.amazonaws.com'
port = '5432'
database = 'd8c1130jk9t7t2'


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
    insert_query = """INSERT INTO player (id, first_name, last_name) VALUES (%s, %s, %s)"""
    test_to_insert = (6, 'test_first_name', 'test_last_name')
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