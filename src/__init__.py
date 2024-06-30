import json

def check():
    print("Checking packing is working .... ")
    

def get_config(key):
    config_file = "/var/labsstorage/home/sanjay/IotFlask/Flask-IOT/config.json" # always use absolute path , not relative path
    file = open(config_file,"r")
    config = json.loads(file.read())

    file.close()

    if key in config:
       
        return config[key]
    else:
        raise Exception("Key {} is not found in config.json".format(key))
    
