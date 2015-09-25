#!/usr/bin/python3.4
#
# A command line tool to get NextTrip information
#
# Chris Moser 09/25/2015
#


# Lets grab some sample bus data

import urllib.request
import xml.etree.ElementTree as ET
import xml.dom.minidom as MD

def getlocations (busNum):
    "This function takes a route number and returns a CSV list of their locations"

    locations = urllib.request.urlopen('http://svc.metrotransit.org/NexTrip/VehicleLocations/' + busNum)
    data = locations.read()
    f = open('locations.xml', 'wb')
    f.write(data)
    f.close()

    xml = MD.parse('locations.xml')
    pretty_xml = xml.toprettyxml()

    print(pretty_xml)

bus = input('Please enter bus number or \"0\" for all: ')
getlocations(bus)
