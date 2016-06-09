import hexchat
import requests
import json

__module_name__ = 'Paste'
__module_author__ = 'OverCoder'
__module_version__ = '0.0.1'
__module_description__ = 'Pastes to pastebin and sends link'

def paste(words, word_eols, userdata):
    req = requests.post("https://p.codebottle.ml/api/v1/paste.php", data = {"code" : word_eols[1]})
    data = json.loads(req.text)
    if data["status"] != "200":
        hexchat.prnt("Paste error: " + data["error"])
    else:
        hexchat.command("say https://" + data["rich_link"])

    return hexchat.EAT_ALL

hexchat.hook_command("PASTE", paste, help="/paste <content> : Pastes to pastebin and sends link")
