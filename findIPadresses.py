#!/usr/bin/env python
__author__ = 'medusa'

import os
try:
    import pygeoip
except ImportError:
    print "[ERROR] No pygeoip installed"
    print "Installing pygeoip..."
    os.system("sudo pip install pygeoip")
    import pygeoip


home = os.environ['HOME']
if not os.path.isfile(home + '/files/GeoLiteCity.dat'):
    print "[ERROR] GeoLiteCity database missing"
    print "Downloading database to " + home + "/files/"
    os.system("cd " + home + " && wget -N -q http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz && gzip -d GeoLiteCity.dat.gz")
print "Thanks to OccupyTheWeb, full tutorial here:  http://null-byte.wonderhowto.com/how-to/hack-like-pro-find-exact-location-any-ip-address-0161964/"
gip = pygeoip.GeoIP(home + '/files/GeoLiteCity.dat')

ip = 0
while ip == 0:
    ip = raw_input("What IP-Adress do you want to trace? ")
    try:
        rec = gip.record_by_addr(ip)
    except socket.error:
        print "[ERROR] Illegal IP address. Try again."
        ip = 0
try:
    lst = rec.items()
except AttributeError:
    print "[ERROR] IP not found."
    exit(0)

for key,val in lst:
    print "%s: %s" %(key,val)
    if key == "longitude":
        long = str(val)
    if key == "latitude":
        lat = str(val)

print "The location on googleMaps:"
print "https://www.google.de/maps/search/" + lat + "+" + long + "/@" + lat + "," + long + ",17z"
