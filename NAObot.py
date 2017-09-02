# -*- coding: utf-8 -*-
import telepot
import time
import random
from telepot.loop import MessageLoop

bot = telepot.Bot("botKEY")

def handle(msg):
	chat_id = msg["chat"]["id"]
	msj = msg["text"]
	msj = msj.lower()
	if "hola" in msj:
		bot.sendMessage(chat_id, "Hello, I'm NAO. My internet address is 192-168-21-128")
	elif "mmm" in msj:
		bot.sendMessage(chat_id, "Fire")
	elif "desastre" in msj or "terrible" in msj or "teggible" in msj:
		bot.sendMessage(chat_id, "Visual Attacker")
	elif "calor" in msj:
		bot.sendMessage(chat_id, "Fire, exclamation mark")
	elif "ofensivo" in msj: 
		bot.sendMessage(chat_id, "UChile Lib")
	elif "pucha" in msj:
		bot.sendMessage(chat_id, "Segmentation Fault")
	elif "rip" in msj:
		bot.sendMessage(chat_id, "Low battery")
	elif "robocup" in msj:
		bot.sendMessage(chat_id, )
	elif "tesis" in msj:
		ans = random.randint(0,3)
		if ans == 0:
			bot.sendPhoto(chat_id,"url")
		elif ans == 1:
			bot.sendPhoto(chat_id,"url")
		elif ans == 2:
			bot.sendPhoto(chat_id,"url")
		elif ans == 3:
			bot.sendPhoto(chat_id,"url")

MessageLoop(bot, handle).run_as_thread()

while 1:
  time.sleep(10)