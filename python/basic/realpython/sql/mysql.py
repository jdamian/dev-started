# pip install mysql-connector-python

import mysql.connector
from mysql.connector import Error

# def create_connection(host_name, user_name, user_password, db_name):
def create_connection(hostname, user_name, user_password):
    con = None
    try:
        con = mysql.connector.connect(
            host=hostname,
            user=user_name,
            passwd=user_password
            # database=db_name
        )
        print('connection to mysql db sucessful')
    except Error as e:
        print(f"the error '{e}' ocurred")
    
    return con

connection = create_connection('localhost','root','021625')


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

create_database_query = "CREATE DATABASE sm_app"
create_database(connection, create_database_query)

connection = create_connection("localhost", "root", "", "sm_app")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT, 
  name TEXT NOT NULL, 
  age INT, 
  gender TEXT, 
  nationality TEXT, 
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""
create_posts_table = """
CREATE TABLE IF NOT EXISTS posts (
  id INT AUTO_INCREMENT, 
  title TEXT NOT NULL, 
  description TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  FOREIGN KEY fk_user_id (user_id) REFERENCES users(id), 
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""

execute_query(connection, create_users_table)
execute_query(connection, create_posts_table)
#
#

# inserting records
create_users = """
INSERT INTO
  `users` (`name`, `age`, `gender`, `nationality`)
VALUES
  ('James', 25, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""

execute_query(connection, create_users)

sql = "INSERT INTO likes ( user_id, post_id ) VALUES ( %s, %s )"
val = [(4, 5), (3, 4)]

cursor = connection.cursor()
cursor.executemany(sql, val)
connection.commit()

# selecting records
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

select_users = "SELECT * FROM users"
users = execute_read_query(connection, select_users)
for user in users:
    print(user)

# updating
update_post_description = """
UPDATE
  posts
SET
  description = "The weather has become pleasant now"
WHERE
  id = 2
"""

execute_query(connection,  update_post_description)

# deleting
delete_comment = "DELETE FROM comments WHERE id = 2"
execute_query(connection, delete_comment)