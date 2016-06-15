import hexchat

__module_name__ = 'Typing'
__module_author__ = 'OverCoder'
__module_version__ = '1.0'
__module_description__ = 'Send /me is typing... when typing'

enabled = False
typing = False

def toggle(words, word_eols, userdata):
    global enabled
    enabled = not enabled
    if enabled:
    	hexchat.prnt("\"Typing...\" is now enabled")
    else:
    	hexchat.prnt("\"Typing...\" is now disabled")

def paste(key, data, userdata):
    global typing
    global enabled
    if not enabled:
        return hexchat.EAT_NONE
    if key[0] == "65293":
        typing = False
    elif not typing:
        typing = True
        hexchat.command("me is typing...")
    return hexchat.EAT_NONE

hexchat.hook_print("Key Press", paste)
hexchat.hook_command("typing", toggle)
