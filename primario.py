import schedule
from gpiozero import CPUTemperature
import matplotlib.pyplot as xyz
from matplotlib import style
import time,psutil 
import os,sys
import datetime

lista=[]
ora=[]
uso=[]
count= int(0)
oldtime = time.time()
def job():

	style.use('ggplot')
	global uso
	global lista
	global ora
	global oldtime
	global count
	count=count+1	
	cpu = CPUTemperature()
	cpu=cpu.temperature
	
	utilizzo=psutil.cpu_percent(interval=1)
	lista.append(cpu)
	ora.append(count)
	uso.append(utilizzo)
	
	

	if time.time() - oldtime > 59:
		xyz.plot(ora,lista, linewidth=2,color='blue')
		xyz.title('Grafico CPU Temperature(C°)')
		xyz.ylabel('Y- CPU Temperature(C°)')
		xyz.xlabel('X- Time(s)')
		try:
			os.system(f'rm //home//pi//Desktop//bot//grafico.png')
			print("File eliminato")
			time.sleep(4)
		except Exception as e:
			print("File NON trovato")
			pass
			
		xyz.savefig('grafico.png')
		
		xyz.clf()
		xyz.plot(ora,uso, linewidth=2,color='red')
		xyz.title('Grafico Utilizzo CPU (%)')
		xyz.ylabel('Y- CPU Usage(%)')
		xyz.xlabel('X- Time(s)')
		try:
			os.system(f'rm //home//pi//Desktop//bot//grafico1.png')
			print("File eliminato")
			time.sleep(4)
		except OSError:
			print("File NON trovato")
			pass
		
			
		xyz.savefig('grafico1.png')
		uso.clear()
		ora.clear()
		lista.clear()
		print("Grafici fatti")
		sys.exit()
		

schedule.every(1).seconds.do(job)

while True:
	schedule.run_pending()
	time.sleep(1)
