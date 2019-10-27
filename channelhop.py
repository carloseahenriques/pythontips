#!/usr/bin/env python3.6                                                                                                                                                     
# -*- coding: utf-8 -*

import threading
import time
import os

def print_hello():
		#os.system('iw dev mon0 set channel 6')
		#os.system('tcpdump -i mon0')
		os.system('./scan.sh')

def print_hi():
		#os.system('iw dev mon0 set channel 9')
		os.system('tcpdump -i mon0 -c 155')

def channel():
		for chn in range(1,14):
			time.sleep(0.08)
			os.system('iw dev mon0 set channel ' +str(chn))
			#print ("tste", chn)
			#print('iw dev mon0 set channel ' +str(chn))
def channeltrue():
		
		while True:
			for chn in range(1,14):
				time.sleep(0.03)
				os.system('iw dev mon0 set channel ' +str(chn))
				#print('iw dev mon0 set channel ' +str(chn))

	
#t1 = threading.Thread(target=print_hello)
#t2 = threading.Thread(target=print_hi)

#t1.start()
#t2.start()
threading.Thread(target=channeltrue).start()
threading.Thread(target=print_hello).start()
#threading.Thread(target=print_hi).start()
#threading.Thread(target=channel).start()


#threading.Thread(target=print_hi2).start()
#hreading.Thread(target=print_hi3).start()

print (threading.main_thread())
print(threading.enumerate())
