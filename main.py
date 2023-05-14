import requests
import os
import time



webhook = input("Webhook: \n")
message = input(("Message: \n"))






















os.system("cls & title [Webhook Spammer] - By: Russian")


while True:
     time.sleep(1)
     r = requests.post(webhook, json={"content": message})
     if r.status_code == 204:
               print("Sent message successfully")
