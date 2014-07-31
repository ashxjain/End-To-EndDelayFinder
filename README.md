####SYNOPSIS:
---------
* End-EndDelay2links.py is a python program to compute end-to-end transmission in a network connecting Host A to Host B via a router R using store and forward switching.
* End-EndDelay3links.py is a python program to compute end-to-end transmission in a network connecting Host A to Host B to Host C via two routers R1,R2 using store and forward switching.

####HOW TO EXECUTE THE PROGRAM WITH ONE EXAMPLE:
--------------------------------------------
**Program execution**:
* To execute the program, specify ./asn1.py and then give input as command line parameters.
* The program is to be invoked as
        
        python End-EndDelay2links.py --t1 <value in Mbps> --t2 <value in Mbps> --d1 <value in KM> --d2 <value in KM> -N <value> -M <value in Mbits> -S <speed in 10^8m/s> -p <processing time in milliseconds>

**Example**:

Input:

        python End-EndDelay2links.py --t1 10 --t2 12 --d1 2 --d2 1 -N 5 -M 19 -S 2 -p 1

Output:

		    Packet          A                            R                           B 
			P1          0.000 ms                  1900.010 ms                  3484.348 ms
			P2       1900.000 ms                  3800.010 ms                  5384.348 ms
			P3       3800.000 ms                  5700.010 ms                  7284.348 ms
			P4       5700.000 ms                  7600.010 ms                  9184.348 ms
			P5       7600.000 ms                  9500.010 ms                 11084.348 ms

		End to End transmission delay = 11084.348 ms

####DESCRIPTION OF HOW THE PROGRAM WORKS:
-------------------------------------
* In this program we are calculating and displaying three things:
	* Time at which packet leaves host A
	* Time at which packet reaches router R
	* Time at which packet reaches host B
* Time at host A for packets is initially taken as 0 for packet 1, and then it is incremented by transmission delay of link1 for each packet. 
* For each packet, transmission and propagation delay of link1 is added to reach router R. Similarly transmission and propagation delay of link2 is added to reach host B.
* If the time taken to reach router R from host A is less than the transmission delay of link2, only then queuing delay is calculated and added. Queuing delay is calculated by adding the difference of transmission delay of link2 and transmission delay of link1 to the time calculated to reach host B.
* In this program we are assuming that router has infinite buffer so there won't be any packet loss. We are not handelling traffic congestion on link in our program. We are not handling traffic congestion on link in our program.

####CHALLENGES FACED AND HOW DID I ADDRESSED IT:
--------------------------------------------
* Displaying N packets if N is too large
	* If N is too large, it gets difficult displaying output so what i did was used string formatting. So i can get predefined columns to display my output.
* Calculating queuing delay
	* It took lots of time to calculate queuing delay. Since i didn't find any question with solution to verify my output, what i did was, I wrote the whole program for 2 routers i.e 3 links and verified the program using the questions and answers from t2 paper. After lots of changes, i changed the code for 1 router. 
* Handling all exceptions
	* It became a problem, since input can be very bad. Handled by adding extra lines of code and by displaying all possible options using help input parameter.   

