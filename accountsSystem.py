print("NEW")

import sqlite3

debug  = False

conn = sqlite3.connect("accounts.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(username TEXT UNIQUE,password TEXT,storedcontent TEXT)")
#cursor.execute("INSERT INTO users VALUES(?,?,?)",("abc","password","hi"))
conn.commit()
if debug:
    print(cursor.execute("SELECT storedcontent FROM users ").fetchone())
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
        validPw = pwToCheck
        pwIsvalid=True
    content= input("enter content to store: ")
    cursor.execute("INSERT INTO users VALUES (?,?,?)", (validName,validPw,content))
    conn.commit()
    print("data saved! log in to view your content!")

def login():
    loginSuccess = False
    while not loginSuccess:
        print("type 'x' to go back")
        nameToCheck = input("enter username: ")
        if nameToCheck == "x":
            break
        pwToCheck = input("enter password: ")
        content = cursor.execute(f"SELECT storedcontent FROM users WHERE username = '{nameToCheck}' AND password = '{pwToCheck}'").fetchone()
        if not content:
            print("password is incorrect or user doesn't exist!")
            continue
        else:
            loginSuccess = True
    if not loginSuccess:
        return
    print("successfully logged in.")
    print(f"\nstored content:\n\n------------------------\n{content[0]}\n------------------------\n")
    cancel = input("continue? ")

def Doprompt():
    global prompt
    print("'x' to stop program")
    prompt = input("Already have an account? [y/n]: ")
    if prompt == "n":
        signup()
    elif prompt == "y":
        login()
    elif prompt == "x":
        print("goodbye!")
        return "x"
    else:
        print("invalid input!")
    return "y"
Doprompt()
while prompt !="x":
    Doprompt()
