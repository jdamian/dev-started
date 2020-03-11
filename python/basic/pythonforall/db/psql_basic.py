import psycopg2

try:
    conn = psycopg2.connect(user="postgres",
                            password="021625",
                            host="localhost",
                            port="5432",
                            database="pentest")
    
    cursor = conn.cursor()
    print(conn.get_dsn_parameters(),"\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if(conn):
        cursor.close()
        conn.close()
        print("PostgreSQL connection is closed")