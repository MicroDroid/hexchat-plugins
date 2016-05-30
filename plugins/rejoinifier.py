import hexchat

__module_name__ = 'Rejoinifier'
__module_author__ = 'OverCoder'
__module_version__ = '0.0.1'
__module_description__ = 'Kick-autorejoin on specific channels'
channels = {}

def kicked(words, word_eols, userdata):
    wait = '0.15' # Increase if your computer is extremely slow (Intel 8080 (kidding))
    channel = hexchat.get_info('channel')
    network = hexchat.get_info('network')
    if channel in channels:
        if ((len(channels[channel]) > 0) & (channels[channel] == network)) | (len(channels[channel]) == 0):
            hexchat.command('timer {} join {}'.format(wait, channel))
            return hexchat.EAT_NONE

def register(words, word_eols, userdata):
    if len(words) < 2:
        hexchat.prnt("You did not specify a channel")
    elif words[1] in channels:
        hexchat.prnt("Removed \002{}\002 from autorejoin list".format(words[1]))
        del channels[words[1]]
    else:
        if len(words) >= 3:
            hexchat.prnt("Autorejoin is now enabled for \002{}\002 on network \002{}\002".format(words[1], words[2]))
            channels[words[1]] = words[2]
        else:
            hexchat.prnt("Autorejoin is now enabled for \002{}\002 on all networks".format(words[1]))
            channels[words[1]] = ""
    return hexchat.EAT_ALL

hexchat.hook_print('You Kicked', kicked)
hexchat.hook_command("AUTOREJOIN", register, help="/autorejoin <channel> [network] ")
