# Created on iPad.

import sqlite3
conn = sqlite3.connect("example.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(username TEXT UNIQUE,password TEXT,storedcontent TEXT)")
#cursor.execute("INSERT INTO users VALUES(?,?,?)",("abc","password","hi"))
conn.commit()

print(cursor.execute("SELECT * FROM users ").fetchall())
def signup():
    nameIsvalid = False
    while not nameIsvalid:
    		nameToCheck = input("enter new username: ")
    		if not nameToCheck:
        		print("username cannot be empty")
        		nameIsvalid = False
        		continue
    		if len(nameToCheck) < 3:
        		print("username must be at least 3 characters long")
        		nameIsvalid = False
        		continue
    		if len(nameToCheck) > 10:
        		print("name is too long! max is 10 characters")
        		nameIsvalid=False
        		continue
    		if cursor.execute(f"SELECT username FROM users WHERE username = '{nameToCheck}'").fetchone():
        		print("username already exists!")
        		nameIsvalid = False
        		continue
    		validName = nameToCheck
    		nameIsvalid = True
    pwIsvalid = False
    while not pwIsvalid:
        pwToCheck = input("create password: ")
        if len(pwToCheck)<6:
            print("password must be at least 6 characters long")
            pwIsvalid = False
            continue
        if len(pwToCheck) > 30:
            print("password is too long. max is 30 characters")
        confirmPw = input("confirm password:  ")
        resetPw = False
        while confirmPw != pwToCheck:
            if confirmPw == "x":
                print("aborted.")
                resetPw=True
                break
            print("passwords do not match! type 'x' to try a new password")
            confirmPw = input("confirm password:  ")
        if resetPw:
            continue
        print("password confirmed!")
        
        
        


prompt = input("Already have an account? [y/n]: ")
if prompt == "n":
    signup()
    