#!/usr/bin/python3

import json
import time

def set_message_send_rate():
    
    return 200
	
def write_to_json(json_path: str, contents: dict):

    try:
        with open(json_path, "w") as outfile: 
            json.dump(contents, outfile,indent = 4)
    except Exception as error:

        pass


def read_json(json_path: str):
    
    try: 
        with open(json_path,"r") as infile:

            return json.load(infile)
    except Exception as error:

        pass

if __name__ == '__main__':
    
    # TODO make this an input argument
    DATA_TRANSFER_MODE = 1   # vm_to_local communications
    # DATA_TRANSFER_MODE = 2  # local_to_local communctions
    
    # control message update rate
    message_speed_hz = set_message_send_rate()
    
    
    # TODO specify in readme that these directories will need to be edited for testing
    if DATA_TRANSFER_MODE == 1:
        JSON_PATH = "/run/user/1000/gvfs/sftp:host=billys-macbook-pro-5.local/Users/billymazotti/github/selected_json_file.json"
    elif DATA_TRANSFER_MODE == 2:
        JSON_PATH = "selected_json_file.json"
    else:
        print("Invalid data transfer mode set")
        
    joint_positions ={
		"timestamp": 0.0,
		"joint_1" : 0.0, 
		"joint_2" : 0.0, 
		"joint_3" : 0.0, 
		"joint_4" : 0.0, 
		"joint_5" : 0.0, 
		"joint_6" : 0.0, 
		"joint_7" : 0.0, 
		"joint_8" : 0.0,
		"joint_9" : 0.0,
		} 

    # Example
    tstart = time.time()
    while True:
        
        # artificially control the message speed
        time.sleep(1/message_speed_hz)
        
        # update the timestamp
        joint_positions["timestamp"] = float(time.time() - tstart)
    
        # update the json file
        write_to_json(JSON_PATH, joint_positions)

        print("timestamp: ", round(joint_positions["timestamp"],3))