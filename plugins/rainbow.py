import hexchat
import random

__module_name__ = 'Rainbows'
__module_author__ = 'OverCoder'
__module_version__ = '0.9'
__module_description__ = 'Send each text with rainbow backgrounds'

enabled = False

def toggle(words, word_eols, userdata):
    global enabled
    enabled = not enabled
    if enabled:
        hexchat.prnt("Rainbow text is now enabled")
    else:
        hexchat.prnt("Rainbow text is now disabled")

def generate_colour(last_colour):
    colour_code = ""
    
    while True:
        colour_code = "\00300," + str(random.randint(1, 12))
        
        if not colour_code == last_colour:
            break
        
    return colour_code

def rainbow(key, data, userdata):
    global enabled
    if not enabled:
        return hexchat.EAT_NONE
    if key[0] == "65293":
        if (hexchat.get_info("inputbox").startswith("/")):
            return hexchat.EAT_NONE
        output = "\002"
        colour = ""
        for word in hexchat.get_info("inputbox").strip(" ").split(" "):
            colour = generate_colour(colour)
            output = output + colour + " " + word + " "
        hexchat.command("say " + output)
        hexchat.command("settext  ")
        return hexchat.EAT_ALL
    return hexchat.EAT_NONE

hexchat.hook_print("Key Press", rainbow)
hexchat.hook_command("rainbow", toggle)
