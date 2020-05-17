#from firebase import Database
from firebase import firebase
import simulator

handler = firebase.FirebaseApplication("https://smartparking-fbb4c.firebaseio.com/")

data = {

    "Request_ID" : "ASDKASJDOKASNCZXKCNOKASD",
    "Allocated slot" : "4"

    }

import time

allocated = [0, 0, 0, 0]
slots = ['slot1', 'slot2', 'slot3', 'slot4']

while(1):

    time.sleep(1)
    test = handler.get('', None)


    j = 0
    for i, value in enumerate(test):
    
        if(test[value] != "" and allocated[i] != 1):
            
            allocated[i] = 1
            #print(allocated, i)
            simulator.down_platform(i+1)
            simulator.add_car()
            


        elif(test[value] == "" and allocated[i] == 1):
            
            allocated[i] = 0
            simulator.down_platform(i+1)
            simulator.remove_car()
            

        #time.sleep(1.5)
            

