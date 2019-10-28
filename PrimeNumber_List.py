#!/usr/bin/env python3.6
# -*- coding: utf-8 -*

import sys

start=int(sys.argv[1])
end=int(sys.argv[2])
'''
for counter in range(2,n):
    if (n % counter == 0):
	    print("Multiplo de", counter)
	    mult +=1
if(mult==0):
    print (n, "é PRIMO")
'''
for counter in range(start, end+1):
	if counter > 1:
		for n in range(2, counter):
			if (counter % n) == 0:
				break
		else:
			print(counter)
			