# bvzm.py
# wewlads, thanks to https://pythonspot.com/en/building-an-irc-bot/ for base code
from irc import *
import os
import random
 
channel = "#bvzm"
server = "chat.freenode.org"
nickname = "bvzmpy"
 
irc = IRC()
irc.connect(server, channel, nickname)
 
 
while 1:
    text = irc.get_text()
    print text
 
    if "PRIVMSG" in text and channel in text and "hello" in text:
        irc.send(channel, "Hello! I am bvzm (python)")
