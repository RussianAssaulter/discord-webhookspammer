import requests
import os
import time

def init(): 
 os.system("cls & title [Webhook Spammer] - By: Russian")
 time.sleep(0.1)
 main()
 

        





def main():
 os.system("cls & title [Webhook Spammer] - By: Russian")
 webhook = input("Webhook: \n")
 message = input(("Message: \n"))
 while True:
     r = requests.post(webhook, json={"content": message})
     if r.status_code == 204:
               print("Sent message successfully")
     elif r.status_code == 429:
        print("Webhook Ratelimited Please Switch Webhooks")
        time.sleep(2)
        main()


init()
