import hexchat
import requests
import json

__module_name__ = 'Paste'
__module_author__ = 'OverCoder'
__module_version__ = '0.8'
__module_description__ = 'Pastes to pastebin and sends link'
command = "/paste"

def paste(key, data, userdata):
    if key[0] == "65293":
        if hexchat.get_info("inputbox").startswith(command):
            hexchat.prnt("Pasting..")
            req = requests.post("https://p.codebottle.ml/api/v1/paste.php", data = {"code" : hexchat.get_info("inputbox")[len(command)+1:]})
            data = json.loads(req.text)
            if data["status"] != "200":
                hexchat.prnt("Paste error: " + data["error"])
            else:
                hexchat.command("say https://" + data["rich_link"])
            return hexchat.EAT_ALL
    return hexchat.EAT_NONE

hexchat.hook_print("Key Press", paste)
