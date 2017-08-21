import telepot
import time
from telepot.loop import MessageLoop

bot = telepot.Bot("botKEY")

def handle(msg):
	chat_id = msg["chat"]["id"]
	msj = msg["text"]
	msj = msj.lower()
	if msj == "hola":
		bot.sendMessage(chat_id, "Hello, I'm NAO. My internet address is 192-168-21-128")
	elif msj == "mmm":
		bot.sendMessage(chat_id, "Fire")
	elif msj == "jaja" or msj == "jajaja":
		bot.sendMessage(chat_id, "Visual Attacker")
	elif msj == "calor":
		bot.sendMessage(chat_id, "Fire, exclamation mark")
	elif msj == "ofensivo": 
		bot.sendMessage(chat_id, "UChile Lib")
	elif msj == "pucha":
		bot.sendMessage(chat_id, "Segmentation Fault")

MessageLoop(bot, handle).run_as_thread()

while 1:
  time.sleep(10)

