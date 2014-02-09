#!/usr/bin/env python
import os
import getopt
import sys

#Transmission Delay
def transDelay(t,M):
	return (M/t)*10**3

#Propagation Delay
def propDelay(d,S):
	return d/(S*100)

def main():
	t1,t2,d1,d2,N,M,S,p = 1,1,1,1,1,1,1,1 #Default
	try:
		opts, args = getopt.getopt(sys.argv[1:],'N:M:S:p:',['t1=','t2=','d1=','d2=','help'])
		if len(opts) == 0 :
			print """Please use the correct arguments, for usage type --help  """
			sys.exit(2)
	except getopt.GetoptError,err:
        	print str(err)
		print """Please use the correct arguments, for usage type --help """
        	sys.exit(2)
	for opt,arg in opts:
		if opt == '--t1':
			t1 = float(arg)
		elif opt == '--t2':
			t2 = float(arg)
		elif opt == '--d1':
			d1 = float(arg)
		elif opt == '--d2':
			d2 =float(arg)
		elif opt == '-N':
			N = float(arg)
		elif opt == '-M':
			M = float(arg)
		elif opt == '-S':
			S = float(arg)
		elif opt == '-p':	
			p = float(arg)
		elif opt == '--help':
			printHelp()
		else:
			assert False, "unhandled option"
	print '\n%10s%5s%9s%20s%9s%20s%9s' % (""," ","+-------+"," "," ------- "," ","+-------+")
	print '%10s%5s%9s%20s%9s%20s%9s' % ("Packet  "," ","|   A   |","-" * 20,"(   R   )","-" * 20,"|   B   |")
	print '%10s%5s%9s%20s%9s%20s%9s' % ("-" * 10," ","+-------+"," "," ------- "," ","+-------+")
	n,A,B,queueDelay= 1,0,0,0
        while n<=N:
                R = A + transDelay(t1,M) + propDelay(d1,S)
		B = R + queueDelay + p + transDelay(t2,M) + propDelay(d2,S)
                if R < transDelay(t2,M):
                        queueDelay = queueDelay + transDelay(t2,M) - transDelay(t1,M)
                print'%10s%2s%9.3f ms%17s%9.3f ms%17s%9.3f ms' % ('P' + `n` + '    ','',A,'',R,'',B)
                n,A = n + 1,A + transDelay(t1,M)
	print "\nEnd to End transmission delay = %9.3f ms\n" %(B)
def printHelp():
	print """We have multiple options:\n\t--t1: Transmission Delay at Link1 <value in Mbps>\n\
	--t2: Transmission Delay at Link2 <value in Mbps>\n\t--d1: Distance of Link1<value in KM>\n\
	--d2: Distance of Link2 <value in KM>\n\t  -N: Number of Packets <value>\n\t  -M: Packet Size <value in Mbits>\n\
	  -S: Propagation Speed <speed in 10^8m/s>\n\t  -p: Router Processing Time <processing time in milliseconds>"""
	sys.exit()
		
if __name__ =='__main__':
	main()
