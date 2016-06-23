#!/usr/bin/env python
__author__ = 'medusa'

import pygeoip

print "Thanks to OccupyTheWeb, full tutorial here:  http://null-byte.wonderhowto.com/how-to/hack-like-pro-find-exact-location-any-ip-address-0161964/"
gip = pygeoip.GeoIP('/home/medusa/misc/geolite/pygeoip-0.1.3/GeoLiteCity.dat')

ip = raw_input("What IP-Adress do you want to trace? ")

rec = gip.record_by_addr(ip)
lst = rec.items()
for key,val in lst:
    print "%s: %s" %(key,val)
    if key == "longitude":
        long = str(val)
    if key == "latitude":
        lat = str(val)

print "The location on googleMaps:"
print "https://www.google.de/maps/search/" + lat + "+" + long + "/@" + lat + "," + long + ",17z"
