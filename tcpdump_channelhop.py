#!/usr/bin/env python3.6                                                                                                                                                     
# -*- coding: utf-8 -*

import threading
import time
import os

def tcpdump():
		#os.system('iw dev mon0 set channel 6')
		os.system('tcpdump -i mon0')

def ChannelHop():
		while True:
			for chn in range(1,14):
				time.sleep(0.03)
				os.system('iw dev mon0 set channel ' +str(chn))
		
threading.Thread(target=ChannelHop).start()
threading.Thread(target=tcpdump).start()

#print (threading.main_thread())
#print(threading.enumerate())
