import telepot
import time
from telepot.loop import MessageLoop

#Ejemplo de un bot repitiendo con el comando /echo

bot = telepot.Bot("botKEY")

def handle(msg):
	chat_id = msg["chat"]["id"]
	msj = msg["text"]
	msj_separado = msj.split(' ', 1)
	comando = msj_separado[0]
	resto = msj_separado[1]
	msj = msj.lower()
	if comando.startswith("/echo"):
		bot.sendMessage(chat_id, resto)


MessageLoop(bot, handle).run_as_thread()

while 1:
  time.sleep(10)

