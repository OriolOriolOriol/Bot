from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
from pathlib import Path
import schedule,time,os
import telegram.ext
import random
import emoji
import requests 
import json,webbrowser
import datetime
from datetime import datetime, timedelta
import smtplib, ssl
from email.mime.text import MIMEText

TOKEN = '790486292:AAE2_Dowg0hRAjypMxlup73MAXOHglv6v2s'
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
def frasi23(update,context):
	frasi1=frasi()
	context.bot.send_message(chat_id=update.effective_chat.id,text=emoji.emojize(":double_exclamation_mark:"))
	context.bot.send_message(chat_id=update.effective_chat.id,text=frasi1)
	context.bot.send_message(chat_id=update.effective_chat.id,text=emoji.emojize(":double_exclamation_mark:"))
	time.sleep(3)
#####################################################

def callback_minute1(context: telegram.ext.CallbackContext):
	
	def send():
		fn = "claudio_note.txt"
		f = open(fn)
		output=[]
		data_adesso=datetime.now()
		data_adesso=str(data_adesso)
		data_adesso=data_adesso[:10]
		data_adesso=datetime.strptime(data_adesso, '%Y-%m-%d').strftime('%d/%m/%Y')
		for myline in f:
			data=myline[:10]
			corpo=myline[10:]
			corpo=str(corpo)
			print(corpo)
			dt_object1 = datetime.strptime(data, "%d/%m/%Y")
			futuredate = dt_object1 - timedelta(days=1)
			futuredate = str(futuredate)
			futuredate = futuredate[:10]
			futuredate1 = dt_object1 - timedelta(days=0)
			futuredate1 = str(futuredate1)
			futuredate1 = futuredate1[:10]
			data_finale=datetime.strptime(futuredate, '%Y-%m-%d').strftime('%d/%m/%Y')
			data_finale1=datetime.strptime(futuredate1, '%Y-%m-%d').strftime('%d/%m/%Y')            
			if data_adesso != data_finale:
				pass
				
			elif data_adesso == data_finale: #or data_adesso == data_finale1:
				port = 587  # For starttls
				smtp_server = "smtp.gmail.com"
				sender_email = "orionperseus999@gmail.com"
				receiver_email = "claudio.rimensi.1996.uni@gmail.com"
				password = "orologio96"
				msg = MIMEText(f'Appuntamento: {str(data)} {str(corpo)}')
				msg['Subject'] = 'Appuntamento immimente!!!'
				msg['From'] = sender_email
				msg['To'] = receiver_email

				context = ssl.create_default_context()
				try:
					with smtplib.SMTP(smtp_server, port) as server:
						server.ehlo()  # Can be omitted
						server.starttls(context=context)
						server.ehlo()  # Can be omitted
						server.login(sender_email, password)
						server.sendmail(sender_email, receiver_email, msg.as_string())
						# tell the script to report if your message was sent or which errors need to be fixed 
						print('Sent')
						
				except (gaierror, ConnectionRefusedError):
					print('Failed to connect to the server. Bad connection settings?')
				except smtplib.SMTPServerDisconnected:
					print('Failed to connect to the server. Wrong user/password?')
				except smtplib.SMTPException as e:
					print('SMTP error occurred: ' + str(e))
			
		f.close
	send()
#####################################################
def callback_minute(context: telegram.ext.CallbackContext):
	hostname="8.8.8.8"
	context.bot.send_message(chat_id='502522267',text='Ti aggiorno sul mio stato di salute..')
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
def business(update,context):
	comando1=f'adb shell screencap -p /sdcard/screencap.png'
	comando2=f'adb pull /sdcard/screencap.png'
	os.system(comando1)
	os.system(comando2)
	time.sleep(2)
	context.bot.send_photo(chat_id=update.effective_chat.id,photo=open('/home/pi/Desktop/bot/screencap.png','rb'))
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="Ricordati che quando ti invio lo screenshot il contatore sara' 10 in meno")
	context.bot.send_message(chat_id=update.effective_chat.id,text=emoji.emojize(":grinning_face_with_smiling_eyes:"))

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
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/nota ")
	time.sleep(1)
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/frasi Frasi motivazionali ")
	time.sleep(1)
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/business")
	time.sleep(1)
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/help: Vi mostro i comandi che potete scrivere perche io vi possa rispondere")
#######################################################################################
def nota(update,context):
	print("Sono entrato nella sezione delle note...\n")
	note=context.args[0:]
	note=" ".join(note)
	if note != "" and note != "cancella":
			
		with open("claudio_note.txt", "a") as file:
			data=file.write(note)
			data=file.write("\n")
			
		time.sleep(1)
		context.bot.send_message(chat_id=update.effective_chat.id,text="Scrittura avvenuta correttamente sul file") 
		context.bot.send_message(chat_id=update.effective_chat.id,text=emoji.emojize(":grinning_face_with_smiling_eyes:"))
		
	elif note == "":
		def delete():
			fn = "claudio_note.txt"
			f = open(fn)
			output=[]
			data_adesso=datetime.now()
			
			for myline in f:
				print(myline)
				data=myline[:10]
				dt_object1 = datetime.strptime(data, "%d/%m/%Y")             
				if dt_object1 < data_adesso:
					pass
					
				elif dt_object1 >= data_adesso:
					output.append(myline)
			
			f.close
			f = open("claudio_note.txt", 'w')
			f.writelines(output)
			f.close()
			
		delete()
		
		with open("claudio_note.txt", "r") as file:
			line = file.readline()
			cnt = 1
			while line:
				testo="Appuntamento {}----> {}".format(cnt, line.strip())
				context.bot.send_message(chat_id=update.effective_chat.id,text=testo) 
				print("Line {}: {}".format(cnt, line.strip()))
				line = file.readline()
				cnt += 1
		

		
		time.sleep(1)
		context.bot.send_message(chat_id=update.effective_chat.id,text="Lettura avvenuta correttamente del file") 
		context.bot.send_message(chat_id=update.effective_chat.id,text=emoji.emojize(":grinning_face_with_smiling_eyes:"))

	
	if note == "cancella":
		file = open("claudio_note.txt", "w").close()
		time.sleep(1)
		context.bot.send_message(chat_id=update.effective_chat.id,text="Eliminazione avvenuta correttamente del contenuto nel file") 
		context.bot.send_message(chat_id=update.effective_chat.id,text=emoji.emojize(":grinning_face_with_smiling_eyes:"))



#########################################################################################
#FUNZIONE PRINCIPALE     
def main():
	print("Sto ascoltando...")
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('help', help1))
	dp.add_handler(CommandHandler('numeri', numeri))
	dp.add_handler(CommandHandler('nota',nota))
	dp.add_handler(CommandHandler('frasi',frasi23))
	dp.add_handler(CommandHandler('password',password,pass_args=True,pass_chat_data=True))
	dp.add_handler(CommandHandler('password1',password1,pass_args=True,pass_chat_data=True))
	dp.add_handler(CommandHandler('meteo',meteo,pass_args=True,pass_chat_data=True))
	dp.add_handler(CommandHandler('business',business))

	job_minute = j.run_repeating(callback_minute, interval=10800, first=0)
	job_minute1 = j.run_repeating(callback_minute1, interval=18000, first=0)
	
	unknown_handler = MessageHandler(Filters.command, unknown)
	dp.add_handler(unknown_handler)
	updater.start_polling()
	updater.idle()


main()
