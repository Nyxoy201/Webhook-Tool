import requests
import time
import pystyle
from pystyle import Colors, Colorate

def send_webhook_message(webhook_url, username, message, num_messages, cooldown, avatar_url=None):
    payload = {
        'username': username,
        'content': message,
        'avatar_url': avatar_url
    }
    print(Colorate.Horizontal(Colors.red_to_yellow,"""
    Spamming..."""))

    for _ in range(num_messages):
        requests.post(webhook_url, json=payload)
        time.sleep(cooldown)

    print(Colorate.Horizontal(Colors.red_to_yellow,"""
    Spamming done."""))

def delete_webhook(webhook_url):
    requests.delete(webhook_url)

print(Colorate.Horizontal(Colors.red_to_yellow, """
  _      __        __    __              __          ____                                      
 | | /| / / ___   / /   / /  ___  ___   / /__       / __/   ___  ___ _  __ _   __ _  ___   ____
 | |/ |/ / / -_) / _ \ / _ \/ _ \/ _ \ /  '_/      _\ \  / _ \/ _ `/ /  ' \ /  ' \/ -_) / __/
 |__/|__/  \__/ /_.__//_//_/\___/\___//_/\_\      /___/ / .__/\_,_/ /_/_/_//_/_/_/\__/ /_/   
                                                       /_/                                                            
                                  BY NYXOY
"""))

webhook_url = input(Colorate.Horizontal(Colors.red_to_yellow, """

Webhook URL : """))
username = input(Colorate.Horizontal(Colors.red_to_yellow, "Webhook Name : "))
message = input(Colorate.Horizontal(Colors.red_to_yellow, "Message : "))
num_messages = int(input(Colorate.Horizontal(Colors.red_to_yellow, "How Many Messages : ")))
cooldown = int(input(Colorate.Horizontal(Colors.red_to_yellow, "Cooldown (0 = no cooldown): ")))
avatar_url = input(Colorate.Horizontal(Colors.red_to_yellow, "Avatar link : "))

send_webhook_message(webhook_url, username, message, num_messages, cooldown, avatar_url)

delete_webhook_input = input(Colorate.Horizontal(Colors.red_to_yellow, """
Do you want to delete the webhook ? (y/n) : """))
if delete_webhook_input.lower() == "y":
    delete_webhook(webhook_url)
    print(Colorate.Horizontal(Colors.red_to_yellow,"    Webhook Deleted."))


