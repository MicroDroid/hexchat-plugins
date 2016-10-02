import hexchat
import requests
import json

__module_name__ = 'Paste'
__module_author__ = 'OverCoder'
__module_version__ = '1.0'
__module_description__ = 'Pastes to a LOLBIN and sends link'
command = "/paste"

def paste(key, data, userdata):
    if key[0] == "65293":
        if hexchat.get_info("inputbox").startswith(command):
            req = requests.post("https://lolbin.nolsen.xyz/", data = {"input":hexchat.get_info("inputbox")[len(command)+1:]}, allow_redirects=False)
            hexchat.command("say https://lolbin.nolsen.xyz/" + req.headers["Location"])
            hexchat.command("settext  ")
            return hexchat.EAT_ALL
    return hexchat.EAT_NONE

hexchat.hook_print("Key Press", paste)
