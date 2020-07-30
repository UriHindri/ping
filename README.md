# Instructions

1. make sure you have python 2.7 installed
2. run "ping.py -h"

--------------------------------------------------------

usage: ping.py [-h] [-c] [-s] [-tcp] [-udp] [-t Timeout] [-n data size]
               [-d IP] -p port

Send or receive ping based on tcp/udp to a selected target

optional arguments:
  -h, --help    show this help message and exit
  -c            run client
  -s            run server
  -tcp          Use TCP for ping check
  -udp          Use UDP for ping check
  -t Timeout    Timeout for connection
  -n data size  size of buffer to send
  -d IP         Destination IP address to check
  -p port       Destination port address to check
  
  
  
for example:

tcp server on port 4000:

ping.py -s -tcp -p 4000


tcp client to localhost on port 4000 with 50 bytes ping and 3 seconds timeout

ping.py -c -tcp -d 127.0.0.1 -p 4000 -n 50 -t 3