import hexchat
import hashlib
import binascii

__module_name__ = 'HashLib'
__module_author__ = 'OverCoder'
__module_version__ = '0.8'
__module_description__ = 'Hash strings on the fly'

def sha1(words, word_eols, userdata):
    hexchat.command("say " + hashlib.sha1(word_eols[1].encode()).hexdigest())

def sha256(words, word_eols, userdata):
    hexchat.command("say " + hashlib.sha256(word_eols[1].encode()).hexdigest())

def sha384(words, word_eols, userdata):
    hexchat.command("say " + hashlib.sha384(word_eols[1].encode()).hexdigest())

def sha512(words, word_eols, userdata):
    hexchat.command("say " + hashlib.sha512(word_eols[1].encode()).hexdigest())

def md5(words, word_eols, userdata):
    hexchat.command("say " + hashlib.md5(word_eols[1].encode()).hexdigest())

def crc32(words, word_eols, userdata):
    hexchat.command("say " + str(binascii.crc32(word_eols[1].encode())))

hexchat.hook_command("sha1", sha1)
hexchat.hook_command("sha256", sha256)
hexchat.hook_command("sha384", sha384)
hexchat.hook_command("sha512", sha512)
hexchat.hook_command("md5", md5)
hexchat.hook_command("crc32", crc32)
