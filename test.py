from src import get_config
from src.User import User
# User.register("sanjay","macbook_air","macbook_air")



try:
    User.login('sanjay','macbook_air')
    print("Login Successfully ")
except Exception as e:
    print("Login Failed ...",e )

