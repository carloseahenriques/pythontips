#!/usr/bin/env python3.6                                                                                                                                                     
# -*- coding: utf-8 -*

import threading
import time
import os

iface = "wlan0mon"

def tcpdump():
		#os.system('iw dev mon0 set channel 6')
		os.system('tcpdump -vvv -e -s0 -i' +iface)

def ChannelHop():
		while True:
			for chn in range(1,14):
				time.sleep(0.04)
				cmd = "iw dev {0} set channel {1}".format(iface, chn)
				os.system(cmd)
				
		
threading.Thread(target=ChannelHop).start()
threading.Thread(target=tcpdump).start()

#print (threading.main_thread())
#print(threading.enumerate())
