import time
import psutil
import os,sys
import matplotlib.pyplot as xyz
from matplotlib import style
import schedule

ul=0.00
dl=0.00
t0 = time.time()
upload=psutil.net_io_counters(pernic=True)['wlan0'][0]
download=psutil.net_io_counters(pernic=True)['wlan0'][1]
up_down=(upload,download)
count=0
upload1=[]
download1=[]
ora=[]
count2=0
ora2=[]

def job():
    
    global upload
    global download
    global upload1
    global download1
    global count
    global ora
    global ora2
    global up_down
    global ul
    global dl
    global t0
    global count2
    style.use('ggplot')
    last_up_down = up_down
    upload=psutil.net_io_counters(pernic=True)['wlan0'][0]
    download=psutil.net_io_counters(pernic=True)['wlan0'][1]
    t1 = time.time()
    up_down = (upload,download)
    try:
        ul, dl = [(now - last) / (t1 - t0) / 1024.0
                 for now,last in zip(up_down, last_up_down)]             
        t0 = time.time()
    except:
        pass
    if dl>0.1 or ul>=0.1:
       count += 1
       count2 += 1
       time.sleep(1)
       ul= "{:0.2f}".format(float(ul))
       dl= "{:0.2f}".format(float(dl))
       if count>2 and count2 >2:
        upload1.append(ul)
        download1.append(dl)
        ora.append(count)
        ora2.append(count2)
       #print('Upload: {:0.2f} kB/s \n'.format(ul)+'Download: {:0.2f} kB/s'.format(dl))
    
    if count==32 and count2==32:
        upload1 = [float(i) for i in upload1]
        new_x, new_y = zip(*sorted(zip(ora,upload1)))
        xyz.plot(new_x,new_y, linewidth=2,color='blue')
        xyz.title('Grafico Upload in (kB\s)')
        xyz.ylabel('Y- Upload in (kB\s)')
        xyz.xlabel('X- Time(s)')
        try:
            os.system(f'rm //home//pi//Desktop//bot//grafico3.png')
            print("File eliminato")
            time.sleep(4)
        except Exception as e:
            print("File NON trovato")
            pass
			
        xyz.savefig('grafico3.png')
        xyz.clf()
        download1 = [float(i) for i in download1]
        new_x1, new_y1 = zip(*sorted(zip(ora2, download1)))
        xyz.plot(new_x1,new_y1, linewidth=2,color='red')
        xyz.title('Grafico Download in (kB\s)')
        xyz.ylabel('Y- Download in (kB\s)')
        xyz.xlabel('X- Time(s)')
		
        try:
            os.system(f'rm //home//pi//Desktop//bot//grafico4.png')
            print("File eliminato")
            time.sleep(4)
        except OSError:
            print("File NON trovato")
            pass
		
        xyz.savefig('grafico4.png')
        upload1.clear()
        ora.clear()
        download1.clear()
        print("Grafici fatti")
        sys.exit()

schedule.every(1).seconds.do(job)

while True:
	schedule.run_pending()
	time.sleep(1)
