from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
from pathlib import Path
import schedule,time,os
import telegram.ext
import random
import emoji
import requests 
import json,webbrowser

TOKEN = '##########################################'
updater = Updater(TOKEN, use_context=True)
j = updater.job_queue
uu=updater.job_queue

###################################################################
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Scusa non ho compreso bene il comando!!")

def leggi_file():
    import random
    lines=open("//home//pi//Desktop/bot//saluti.txt").read().splitlines()
    myline =random.choice(lines)
    return myline


def frasi():
    import random
    lines=open("//home//pi//Desktop/bot//frasi.txt").read().splitlines()
    myline =random.choice(lines)
    return myline
##########################################################
def check():
	hostname="8.8.8.8"
	time.sleep(1)
	os.system(f'python3 //home//pi//Desktop//bot//primario.py')
	time.sleep(1)
	try:
		response=os.system(f'ping -c 3 {hostname}')
		if response ==0:
			print("ATTIVA")
			time.sleep(1)
			os.system(f'python3 //home//pi//Desktop//bot//ciao.py')
			time.sleep(1)
			
		else:
			print("NON ATTIVA")
			context.bot.sendMessage(chat_id=update.effective_chat.id,text="La rete non e' attiva")
			context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":face_with_head-bandage:"))
			
	except socket.timeout:
		context.bot.sendMessage(chat_id=update.effective_chat.id,text="Socket timeout..Rinviami il messaggio")
		context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":pensive_face:"))


##########################################################
def password(update,context):
	 context.bot.sendMessage(chat_id=update.effective_chat.id,text="Ciao Claudio benvenuto nel tuo gestore password")
	 context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":grinning_face_with_smiling_eyes:"))
	 time.sleep(1)
	 esistenza=os.path.exists('//home//pi//Desktop//bot//(encrypted)pass.txt')
	 try:
		 elimina="rm" + " " + "//home//pi//Desktop//bot//pass.txt"
		 os.system(elimina)
	 except OSError:
		 pass

	 if esistenza == True:
		 password1=context.args[0]
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text="Il file e' criptato...")
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":zipper-mouth_face:"))
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text="Avvio processo di decriptazione...")
		 programma="python" + " " + "//home//pi//Desktop//bot//password.py" + " " + password1
		 os.system(programma)
		 file=open("pass.txt","r")
		 riga=file.read()
		 pass1=context.bot.sendMessage(chat_id=update.effective_chat.id,text=riga)
		 time.sleep(2)
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text="Invio password completata")
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":grinning_face_with_smiling_eyes:"))
		 time.sleep(20)
		 #eliminazione messaggio utente
		 context.bot.deleteMessage(chat_id=update.effective_chat.id,message_id=update.message.message_id)
		 #eliminazione messaggio ultimo bot
		 context.bot.deleteMessage(chat_id=update.effective_chat.id,message_id=pass1['message_id'])
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text="Password cancellate")
		 programma="python" + " " + "//home//pi//Desktop//bot//password.py" + " " + password1
		 os.system(programma)
		 elimina="rm" + " " + "//home//pi//Desktop//bot//pass.txt"
		 os.system(elimina)
		 
	 else:
		 bot.sendMessage(chat_id,"Il file e' decriptato...")
		 password1=context.args[0]
		 programma="python" + " " + "//home//pi//Desktop//bot//password.py" + " " + password1
		 os.system(programma)
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text="Il file e' criptato...")
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":zipper-mouth_face:"))
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text="Avvio processo di decriptazione...")
		 programma="python" + " " + "//home//pi//Desktop//bot//password.py" + " " + password1
		 os.system(programma)
		 file=open("pass.txt","r")
		 riga=file.read()
		 pass1=bot.sendMessage(chat_id,riga)
		 time.sleep(2)
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text="Invio password completata")
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":grinning_face_with_smiling_eyes:"))
		 time.sleep(20)
		 #eliminazione messaggio utente
		 context.bot.deleteMessage(chat_id=update.effective_chat.id,message_id=update.message.message_id)
		 #eliminazione messaggio ultimo bot
		 context.bot.deleteMessage(chat_id=update.effective_chat.id,message_id=pass1['message_id'])
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text="Password cancellate")
		 programma="python" + " " + "//home//pi//Desktop//bot//password.py" + " " + password1
		 os.system(programma)
		 elimina="rm" + " " + "//home//pi//Desktop//bot//pass.txt"
		 os.system(elimina)
##################################################################################
def password1(update,context):
	 context.bot.sendMessage(chat_id=update.effective_chat.id,text="Ciao Eleonora benvenuta nel tuo gestore password")
	 context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":grinning_face_with_smiling_eyes:"))
	 time.sleep(1)
	 esistenza=os.path.exists('//home//pi//Desktop//bot//(encrypted)pass_ele.txt')
	 try:
		 elimina="rm" + " " + "//home//pi//Desktop//bot//pass_ele.txt"
		 os.system(elimina)
	 except OSError:
		 pass

	 if esistenza == True:
		 password1=context.args[0]
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text="Il file e' criptato...")
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":zipper-mouth_face:"))
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text="Avvio processo di decriptazione...")
		 programma="python" + " " + "//home//pi//Desktop//bot//password1.py" + " " + password1
		 os.system(programma)
		 file=open("pass_ele.txt","r")
		 riga=file.read()
		 pass1=context.bot.sendMessage(chat_id=update.effective_chat.id,text=riga)
		 time.sleep(2)
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text="Invio password completata")
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":grinning_face_with_smiling_eyes:"))
		 time.sleep(20)
		 #eliminazione messaggio utente
		 context.bot.deleteMessage(chat_id=update.effective_chat.id,message_id=update.message.message_id)
		 #eliminazione messaggio ultimo bot
		 context.bot.deleteMessage(chat_id=update.effective_chat.id,message_id=pass1['message_id'])
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text="Password cancellate")
		 programma="python" + " " + "//home//pi//Desktop//bot//password1.py" + " " + password1
		 os.system(programma)
		 elimina="rm" + " " + "//home//pi//Desktop//bot//pass_ele.txt"
		 os.system(elimina)
		 
	 else:
		 bot.sendMessage(chat_id,"Il file e' decriptato...")
		 password1=context.args[0]
		 programma="python" + " " + "//home//pi//Desktop//bot//password1.py" + " " + password1
		 os.system(programma)
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text="Il file e' criptato...")
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":zipper-mouth_face:"))
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text="Avvio processo di decriptazione...")
		 programma="python" + " " + "//home//pi//Desktop//bot//password1.py" + " " + password1
		 os.system(programma)
		 file=open("pass_ele.txt","r")
		 riga=file.read()
		 pass1=bot.sendMessage(chat_id,riga)
		 time.sleep(2)
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text="Invio password completata")
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":grinning_face_with_smiling_eyes:"))
		 time.sleep(20)
		 #eliminazione messaggio utente
		 context.bot.deleteMessage(chat_id=update.effective_chat.id,message_id=update.message.message_id)
		 #eliminazione messaggio ultimo bot
		 context.bot.deleteMessage(chat_id=update.effective_chat.id,message_id=pass1['message_id'])
		 context.bot.sendMessage(chat_id=update.effective_chat.id,text="Password cancellate")
		 programma="python" + " " + "//home//pi//Desktop//bot//password1.py" + " " + password1
		 os.system(programma)
		 elimina="rm" + " " + "//home//pi//Desktop//bot//pass_ele.txt"
		 os.system(elimina)


############################################################################
def meteo(update,context):
	saluto=leggi_file()
	context.bot.sendMessage(chat_id=update.effective_chat.id, text='%s Eleonora e Claudio, sono Perseus a vostra disposizione!!!'%saluto)
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":grinning_face_with_smiling_eyes:"))
	try:
		try:
			city_name=context.args[0:]
			city_name=" ".join(city_name)
			print(city_name)
			context.bot.sendMessage(chat_id=update.effective_chat.id,text= 'Previsioni del meteo per %s' %city_name)
			api_key = "58f1e77f68f6dfc6ab53cadc0092c4a6"
			base_url = "http://api.openweathermap.org/data/2.5/weather?"
			complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
			response = requests.get(complete_url) 
			x = response.json()
			y = x['main']
			current_temperature=y['temp']
			current_temperature=str((current_temperature-273.15))
			current_humidity = str(y["humidity"])
			z= x['weather']
			descrizione=z[0]["description"]
			n=x['wind']
			vento=n["speed"]
			time.sleep(1)
			#PARAMETRI METEO
			context.bot.sendMessage(chat_id=update.effective_chat.id,text="Temperatura: %s Gradi" %current_temperature)
			context.bot.sendMessage(chat_id=update.effective_chat.id,text="Umidita: %s %%" %current_humidity)
			context.bot.sendMessage(chat_id=update.effective_chat.id,text="Velocita Vento: %s m/s" %vento)
			context.bot.sendMessage(chat_id=update.effective_chat.id,text="Descrizione: %s" %descrizione) 
			#TIPI DI METEO
			if descrizione=="clear sky" or descrizione=="sun":
				context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":sun:"))
			elif  descrizione=="Cloudy" or descrizione=="cloud" or descrizione=="scattered clouds" or descrizione=="broken clouds" or descrizione=="overcast clouds":
				context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":cloud:"))
			elif descrizione=="haze" or descrizione=="Haze" or descrizione== "mist" or descrizione=="Mist":
				context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":fog:"))
			elif descrizione=="few cloud" or descrizione=="few clouds":
				context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":sun_behind_cloud:"))
			elif descrizione=="light rain" or descrizione=="rain" or descrizione=="shower rain" or descrizione=="light intensity shower rain" or descrizione=="moderate rain":
				context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":cloud_with_rain:"))
			elif descrizione=="thunderstorm" or descrizione=="thunderstorm with light rain":
				context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":cloud_with_lightning_and_rain:"))
			elif descrizione=="snow" or descrizione=="light snow":
				context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":cloud_with_snow:"))
			
		except  socket.timeout:
			context.bot.sendMessage(chat_id=update.effective_chat,text="Socket timeout..Rinviami il messaggio")
			context.bot.sendMessage(chat_id=update.effective_chat,text=emoji.emojize(":pensive_face:"))
	
	except KeyError:
		context.bot.sendMessage(chat_id=update.effective_chat.id,text="Nome citta errato oppure scrivila in Inglese...")

######################################################################
def numeri(update,context):
	 saluto=leggi_file()
	 context.bot.sendMessage(chat_id=update.effective_chat.id, text='%s Eleonora e Claudio, sono Perseus a vostra disposizione!!!'%saluto)
	 context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":grinning_face_with_smiling_eyes:"))
	 context.bot.sendMessage(chat_id=update.effective_chat.id,text="Ecco a voi i numeri...")
	 l = []
	 while len(l) < 6:
		 numero = random.randint(1,90)
		 if numero not in l:
			 l.append(numero)
			 numero=str(numero)
			 context.bot.sendMessage(chat_id=update.effective_chat.id,text="%s" %numero)
			 time.sleep(1)
	 context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":grinning_face_with_smiling_eyes:"))

####################################################
def callback_minute1(context: telegram.ext.CallbackContext):
	frasi1=frasi()
	context.bot.send_message(chat_id='502522267',text=emoji.emojize(":double_exclamation_mark:"))
	context.bot.send_message(chat_id='502522267',text=frasi1)
	context.bot.send_message(chat_id='502522267',text=emoji.emojize(":double_exclamation_mark:"))
	time.sleep(3)
#####################################################
def callback_minute(context: telegram.ext.CallbackContext):
	hostname="8.8.8.8"
	context.bot.send_message(chat_id='502522267',text='Fra qualche minuto riceverai il grafico della Uso e della Temperatura della CPU...')
	context.bot.send_message(chat_id='502522267',text='Ti saranno inviati anche i grafici relativi all Upload e Download (Kb\s)...')
	response=os.system(f'ping -c 3 {hostname}')
	if response ==0:
		context.bot.send_message(chat_id='502522267',text="La rete is UP") 
		context.bot.send_message(chat_id='502522267',text=emoji.emojize(":grinning_face_with_smiling_eyes:")) 
		check()
	else:
		context.bot.send_message(chat_id='502522267',text="La rete is DOWN")
		context.bot.send_message(chat_id='502522267',text=emoji.emojize(":face_with_head-bandage:"))
	
	context.bot.send_photo(chat_id='502522267',photo=open('//home//pi//Desktop//bot//grafico.png', 'rb'))
	context.bot.send_photo(chat_id='502522267',photo=open('//home//pi//Desktop//bot//grafico1.png', 'rb'))
	context.bot.send_photo(chat_id='502522267',photo=open('//home//pi//Desktop//bot//grafico3.png', 'rb'))
	context.bot.send_photo(chat_id='502522267',photo=open('//home//pi//Desktop//bot//grafico4.png', 'rb'))
	
###########################################################
def help1(update,context):
	context.bot.sendMessage(chat_id=update.effective_chat.id,text='Ecco quello che posso fare per voi, per adesso...')
	time.sleep(1)
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/meteo [nome_citta]: Vi do le previsioni del meteo della citta che volete")
	time.sleep(1)
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/numeri: Vi do random 6 numeri se volete giocare al superenalotto :) Che la fortuna possa essere sempre dalla vostra parte")
	time.sleep(1)
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/password [password_Claudio]")
	time.sleep(1)
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/password1 [password_Eleonora]")
	time.sleep(1)
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/dati ")
	time.sleep(1)
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/help: Vi mostro i comandi che potete scrivere perche io vi possa rispondere")
#######################################################################################
def dati1(update,context):
	print("Sono entrato nella sezione dati...\n")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="Ti invio il file relativo all'attività sul tuo pc..")
	time.sleep(1)
	delete="rm" + " " + "-rf" + " " + "//home//pi//Desktop//bot//event_log//log"
	os.system(delete)
	os.chdir("//home//pi//Desktop//bot//event_log")
	clono="git" + " " + "clone" + " " + "https://github.com/OriolOriolOriol/log.git"
	os.system(clono)
	print("Ho clonato")
	context.bot.send_document(chat_id=update.effective_chat.id,document=open('//home//pi//Desktop//bot//event_log//log//log1234.txt','rb'))
	time.sleep(1)
	print("File inviato")
	context.bot.send_message(chat_id=update.effective_chat.id,text="File inviato correttamente") 
	context.bot.send_message(chat_id=update.effective_chat.id,text=emoji.emojize(":grinning_face_with_smiling_eyes:"))


#########################################################################################
#FUNZIONE PRINCIPALE     
def main():
	print("Sto ascoltando...")
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('help', help1))
	dp.add_handler(CommandHandler('numeri', numeri))
	dp.add_handler(CommandHandler('dati',dati1))
	dp.add_handler(CommandHandler('password',password,pass_args=True,pass_chat_data=True))
	dp.add_handler(CommandHandler('password1',password1,pass_args=True,pass_chat_data=True))
	dp.add_handler(CommandHandler('meteo',meteo,pass_args=True,pass_chat_data=True))
	
	job_minute = uu.run_repeating(callback_minute1, interval=7200, first=0)
	job_minute = j.run_repeating(callback_minute, interval=10800, first=0)
	#evento sconosciuto
	unknown_handler = MessageHandler(Filters.command, unknown)
	dp.add_handler(unknown_handler)
	updater.start_polling()
	updater.idle()


main()
