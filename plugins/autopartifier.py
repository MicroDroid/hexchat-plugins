import hexchat
from time import time

__module_name__ = 'Autopartifier'
__module_author__ = 'OverCoder'
__module_version__ = '0.0.1'
__module_description__ = 'Auto part channels after being idle for some time'
channels = {}

def check(data):
    for channelName in channels:
        channel = channels[channelName]
        if (((time() * 1000) - channel[1]) > channel[0]):
            channel_joined = False
            for chan in hexchat.get_list("channels"):
                if chan.channel == channelName:
                    channel_joined = True
            if channel_joined:
                hexchat.command("PART " + channelName)
                del channels[channelName]
    return 1

def register(words, word_eols, userdata):
    if len(words) < 2:
        hexchat.prnt("You did not specify a channel")
    elif len(words) < 3:
        hexchat.prnt("You did not specify timeout");
    elif words[1] in channels:
        hexchat.prnt("Removed \002{}\002 from autopart list".format(words[1]))
        del channels[words[1]]
    else:
        hexchat.prnt("Autopart is now enabled for \002{}\002, parting after being idle for \002{}\002 seconds".format(words[1], words[2]))
        channels[words[1]] = (float(words[2]), time() * 1000)
    return hexchat.EAT_ALL

def refresh(words, word_eols, userdata):
    channel = hexchat.get_info("channel")
    if channel in channels:
        channels[channel] = (channels[channel][0], time() * 1000)

def parted(words, word_eols, userata):
    channel = hexchat.get_info("channel")
    if channel in channels:
        del channels[channel]

hexchat.hook_timer(3000, check) # Change as you like, it's in ms
hexchat.hook_command("autopart", register, help="/autopart <channel> <timeout> Part a channel after being idle for n seconds")
hexchat.hook_print("Your Message", refresh)
hexchat.hook_print("You Part with Reason", parted)
hexchat.hook_print("You Part", parted)
