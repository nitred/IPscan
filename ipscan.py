#To Scan all ips in network via TCP.

import urllib2
import time
import socket
import sys


IP_COUNT = 100
IP_LIST = []
#TIMEOUT TIME FOR ONE HTTP REQUEST
TIMEOUT = 1

url_base = 'http://192.168.0.'

def IP_Finder():
    for i in range(IP_COUNT):
        global IP_LIST

        error_flag = False

        print i+1, ":"
        url = url_base + str(i+1)
        #url = url_base + str(100)
        
        try:
            print urllib2.urlopen(url, timeout=1).read()
        except urllib2.HTTPError, e:
            print e.code
            error_flag = True
        except urllib2.URLError, e:
            print e.args
            error_flag = True
        except socket.timeout, e:
            print e.args
            error_flag = True

        if not error_flag:
            IP_LIST.append(i+1)
            print "FOUND ONE"
        else:
            print "FOUND ERROR"
        print IP_LIST

    print "These are the IPs Found"
    print IP_LIST

if __name__ == "__main__":
    IP_Finder()
    print "Exit"
    sys.exit()

    
