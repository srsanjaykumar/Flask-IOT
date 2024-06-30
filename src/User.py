from src.Database import Database
from time import time 
from random import randint
import bcrypt

db = Database.get_connection()
users = db.users # if collections doesn't exist  it will create new collection 


class User:
    def __init__(self , id ) -> None:
        print('Init user with {} '.format(id))
        # build a user object if user is avaliable 

    @staticmethod
    def login(username, password):
        result = users.find_one({"username":username})

        if result:
            # print("===",dict(result))
            # print(result.keys())
            # if result['password'] == password:
            #     return True
            # else:
            #     raise Exception("Invalid password ")

            hashedpw = result['password']
            if bcrypt.checkpw(password.encode() , hashedpw ):
                #TODO : Register a session and return a session ID  on successful Login 
                return True
            else:
                raise Exception("Incorrect Password ")

        else:
            raise Exception("Invalid Credenetials")

    @staticmethod 
    def register(username, password,confirm_password):
        #TODO : avoid duplicate signups 


        if len(password) != len(confirm_password):
            raise Exception("Password length does not match .. please check password ...  ")
        if confirm_password != password:
            raise Exception("Password and Confirm Password does not match ")
        password = password.encode()
        print("Encode password : ", password)

        salt = bcrypt.gensalt()
        print("salt : ",salt)

        password = bcrypt.hashpw(password,salt)
        print("hashed password : ",password)

        id = users.insert_one({
            "username":username, #TODO : make unique index to  avoid duplicate entries 
            "password":password,
            "register_time":time(),
            "active":False,
            "active_token":randint(100000,999999)
        })

        return id 
    

        