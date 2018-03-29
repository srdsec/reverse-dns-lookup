#!/usr/bin/env python
#
# @name:    Simple ip2domain Converter Script
# @repo:    NA
# @author:  Shane Daniels (PBCT3CH)
# Notes:  ip2domian.py will take in a file with ip addresses and externally resolve the domain name via dns lookup.
#         Known problems running on MacOS v10.13.3

import socket

inFilePath = input("Please enter path to Input File: ")
inFile = open(inFilePath,'r')

for ip in inFile.readlines():
    dns = socket.gethostbyaddr(ip)
    print (dns)
inFile.close()
