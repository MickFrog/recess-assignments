# Ssenono Jordan Michael
# 21/U/1013
# 2100701013

import sqlite3  # for db operations

# for multithreading and multiprocessing ops
import time
import threading
import multiprocessing

############################################################################
print("############## File Handling Context Manager ######################")
############################################################################


class FileOpener:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


# Using the file handling class
with FileOpener('example.txt', 'w') as file:
    contents = file.write("Kalooli Lwanga")
    print(contents)


############################################################################
print("########################### Database Context Manager ######################")
############################################################################


class DatabaseHandler:
    def __init__(self, database):
        self.database = database
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.database)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


# USing the db handler:
with DatabaseHandler('example.db') as conn:
    cursor = conn.cursor()

    # Execute SQL queries
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS employees (id INTEGER, name TEXT)")
    cursor.execute("INSERT INTO employees VALUES (1, 'Jeff Geoff')")
    cursor.execute("INSERT INTO employees VALUES (2, 'Kalooli Lwanga')")
    cursor.execute("SELECT * FROM employees")

    # Fetch and print the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)


############################################################################
print("################ Multithreading and MultiProcessing ##################")
############################################################################


def task(duration, caller):
    print(f"{caller} running for {duration} seconds.")
    time.sleep(duration)
    print(f"{caller} completed after {duration} seconds.")

if __name__ == '__main__':
    # Multithreading 
    thread1 = threading.Thread(target=task, args=(3, "Thread 1"))
    thread2 = threading.Thread(target=task, args=(5, "Thread 2"))
    thread1.start()
    thread2.start()

    # Multiprocessing 
    process1 = multiprocessing.Process(target=task, args=(3, "Process 1"))
    process2 = multiprocessing.Process(target=task, args=(5, "Process 2"))
    process1.start()
    process2.start()


# Lessons learnt 
# Learnt the importance of context in programming to ensure efficient use of majorly shared resources 
# USing SQLite for simple db opeartion without needing an actual db, can be essential for testing actual db interaction without 
#   making actual calls to the real db

# MultiThreading - good for simultaneous I/O bound operations due to Python Global Interpreter Lock(GIL) which forces sequential 
#   execution of threads

# MultiProcessing - good for simultaneous CPU bound ops as it bypasses Python's GIL since each process has its own interpreter instance
#   and alow real pralle processing on multi core CPUs