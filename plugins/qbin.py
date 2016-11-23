import hexchat
import requests
import json

__module_name__ = 'qbin'
__module_author__ = 'OverCoder'
__module_version__ = '1.1'
__module_description__ = 'Pastes to qbin and sends link'
command = "/qbin"

def paste(key, data, userdata):
	if key[0] == "65293":
		if hexchat.get_info("inputbox").startswith(command):
			try:
				req = requests.post("https://qbin.io/", {"Q": hexchat.get_info("inputbox")[len(command)+1:]})
				hexchat.command("say " + req.text)
				hexchat.command("settext  ")
			except:
				hexchat.command("settext  ")
			return hexchat.EAT_ALL
	return hexchat.EAT_NONE

hexchat.hook_print("Key Press", paste)
