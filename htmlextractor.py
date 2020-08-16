import sys
import os
import json
import  requests
os.system("clear")
os.system( "toilet -f smmono12 -F metal Html Extractor")
print
print      'Author  :  Rahat Khan Tusar(RKT)'
print
print      'Github  : https://github.com/r3k4t'
print
print 'Information  :  Use vpn/openvpn/tor/tor proxy network.Be anonymous.'
print
url=raw_input("Target Url : ")
print
resp=requests.get(url)
print (resp.json)
print (resp.text)
