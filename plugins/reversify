import hexchat

__module_name__ = 'Reversifier'
__module_author__ = 'OverCoder'
__module_version__ = '0.0.1'
__module_description__ = 'Output text in a reversed way'

def reverse(words, word_eols, userdata):
    hexchat.command("SAY {}".format(word_eols[1][::-1]))
    return hexchat.EAT_ALL

hexchat.hook_command("REVERSE", reverse, help="/reverse <message> Reverses the text! yay!")
