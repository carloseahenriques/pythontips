

import sys
n=int(sys.argv[1])
mult=0

for counter in range(2,n):
    if (n % counter == 0):
	    print("Multiplo de", counter)
	    mult +=1
if(mult==0):
    print (n, "é PRIMO")
