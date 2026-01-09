#!/usr/bin/python3
"""
Creates the database alx_book_store in a MariaDB server.
"""

import MySQLdb

def create_database():
    connection = None
    try:
        connection = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="peter"
        )

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
        print("Database 'alx_book_store' created successfully!")

    except MySQLdb.Error as e:
        print(f"Error while connecting to database: {e}")

    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
