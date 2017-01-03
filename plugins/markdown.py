import hexchat
import re

__module_name__ = 'Markdown'
__module_author__ = 'OverCoder'
__module_version__ = '0.4.3'
__module_description__ = 'Parses incoming and outgoing markdown to IRC attributes'
command = 'markdown'
command_help = """
Usage:
    /markdown <action> <params...>

List of actions:
    /markdown config
        Prints current stored configuration
    /markdown config help
        Prints available configurations
    /markdown config set <key> <value>
        Sets configuration parameter
    /markdown config unset <key>
        Deletes a configuration parameter
"""
config_prefix = 'markdown_'
available_config = {
    'parse_incoming': 'Parse incoming messages [true]',
    'parse_outgoing': 'Parse outgoing messages [true]'
}

positive_input = ['yes', 'yas', 'yeah', 'true', '1', 'on', 'y']

emitting = False

def parse(markdown):
    # I am not using a markdown library because we don't need to parse eveything
    # Markdown offers. And this is just faster and more efficient in our case
    # 
    # Every rule has a comment describing what it parses. And it's self-descriptive even.
    if (markdown[:2] == '> '):
        return '\x0303▍ ' + markdown[2:]
    stylingMaps = {
        '`': '\x0300,01 {} \x03',
        '**': '\x02{}\x02',
        '*': '\x1d{}\x1d',
        '_': '\x1d{}\x1d',
    }
    result = markdown
    for char, template in stylingMaps.items():
        char = re.escape(char)
        result = re.sub('([^\\\]*)' + char + '([^' + char + ']*[^\\\])' + char, '\g<1>' + template.replace('{}', '\g<2>'), result)
    return result

def onCommand(words, words_eol, userdata):
    if (len(words) < 2):
        print(command_help)
    else:
        if words[1] == 'config':
            if len(words) > 2:
                if words[2] == 'help':
                    result = '\n'.join(['   ' + key + '  =>  ' + value for key, value in available_config.items()])
                    print('Available configuration:\n\n' + result)
                elif words[2] == 'set':
                    if (len(words) < 5):
                        print(command_help)
                    else:
                        hexchat.set_pluginpref(config_prefix + words[3], words_eol[4])
                        print(words[3] + ':' + words_eol[4])
                elif words[2] == 'unset':
                    if (len(words) < 4):
                        print(command_help)
                    else:
                        hexchat.del_pluginpref(config_prefix + words[3])
                        print(words[3] + ' has been unset')
                else:
                    print(command_help)
            else:
                prefs_list = hexchat.list_pluginpref()
                result = '{\n'
                for pref in prefs_list:
                    if pref[:9] == config_prefix:
                        result = result + '    ' + pref[len(config_prefix):] + ':' + hexchat.get_pluginpref(pref) + '\n'
                result = result + '}'
                print(result)
        else:
            print('wat')
    return hexchat.EAT_ALL

def onChannelMessage(params, data, userdata):
    global emitting
    if emitting or not hexchat.get_pluginpref('parse_outgoing') in positive_input:
        return hexchat.EAT_NONE
    emitting = True
    params[1] = parse(params[1])
    hexchat.emit_print('Channel Message', params[0], params[1])
    emitting = False
    return hexchat.EAT_ALL

def onSendingMessage(words, words_eol, userdata):
    global emitting
    if emitting or not hexchat.get_pluginpref('parse_incoming') in positive_input:
        return hexchat.EAT_NONE
    emitting = True
    result = parse(words_eol[0])
    hexchat.command('say ' + result)
    emitting = False
    return hexchat.EAT_ALL


hexchat.hook_command(command, onCommand, help=command_help)
hexchat.hook_command('', onSendingMessage)
hexchat.hook_print('Channel Message', onChannelMessage)
