from app.mac import mac, signals
import os
os.chdir("/home/akshit/Documents/TomTomB/ChatBot")
from ChatBot import Bot_Outputs
from TomTomAPI import TomAPI
'''
Signals this module listents to:
1. When a message is received (signals.command_received)
==========================================================
'''
@signals.message_received.connect
def handle(message):
    a = Bot_Outputs.classify(message.text)
    if message.text.lower() == "hi":
        hi(message)
    elif message.text.lower() == "help": 
        help(message)
    elif a[0][0] == "home":
        mac.send_message(TomAPI.home(), message.conversation)
    elif a[0][0] == "goodbye":
        mac.send_message(TomAPI.goodbye(), message.conversation)
    elif a[0][0] == "thanks":
        mac.send_message(TomAPI.thanks(), message.conversation)
    elif a[0][0] == "reminder":
        mac.send_message(TomAPI.reminder(), message.conversation)
    elif a[0][0] == "Reachable_Range":
        mac.send_message(TomAPI.range(), message.conversation)
    elif a[0][0] == "route":
        mac.send_message(TomAPI.route(), message.conversation)
    elif a[0][0] == "Nearby":
        mac.send_message(TomAPI.nearby(), message.conversation)
    elif a[0][0] == "Traffic":
        mac.send_message(TomAPI.traffic(), message.conversation)
    

'''
Actual module code
==========================================================
'''
def hi(message):
    who_name = message.who_name
    answer = "Hi " + who_name + "\n\nWelcome to TomTom WhatsBot Demo \n\nType help to know about the features"
    mac.send_message(answer, message.conversation)
    
def help(message):
    answer = "*TomTom WhatsBot Demo* \n\n1. Calculate when you have to leave in order to arrive on time \n\n2. Search Nearby Places and know how long will it take to reach there \n\n3. Check the distance and travel time between two places \n\n4. Calculate how far can your vehicle go with the fuel you have"
    mac.send_message(answer, message.conversation)