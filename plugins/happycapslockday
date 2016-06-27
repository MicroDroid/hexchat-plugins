import hexchat

__module_name__ = 'Happy Caps Lock Day'
__module_author__ = 'OverCoder'
__module_version__ = '0.9'
__module_description__ = 'Capitalize all text on specified channels'
channels = []

def register(words, word_eols, userdata):
    if len(words) < 2:
        hexchat.prnt("You did not specify a channel")
    elif words[1] in channels:
        hexchat.prnt("Removed \002{}\002 from caps list".format(words[1]))
        channels.remove(words[1])
    else:
        hexchat.prnt("Capitalization is now enabled for \002{}\002".format(words[1]))
        channels.append(words[1])
    return hexchat.EAT_ALL

def send(key, data, userdata):
    if key[0] == "65293":
        user_input = hexchat.get_info("inputbox");
        if hexchat.get_info("channel") in channels:
            if user_input.startswith("/") and not user_input.startswith("/me"):
                return hexchat.EAT_NONE
            hexchat.command("say {}".format(user_input.upper()))
            hexchat.command("settext  ")
            return hexchat.EAT_ALL
    return hexchat.EAT_NONE

hexchat.hook_command("caps", register, help="/caps <channel> : Capitalize all text sent to the specified channel")
hexchat.hook_print("Key Press", send)
