#!/usr/local/bin/python3
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
    "This function takes a route number and returns a GeoJSON Multipoint array of vehicle locations"

    locations = urllib.request.urlopen('http://svc.metrotransit.org/NexTrip/VehicleLocations/' + busNum)
    data = locations.read()
    root = ET.fromstring(data)

    print("This is what I think the answer should be")
    for vehicle in root:
        lat = vehicle.find('VehicleLatitude')
        lon = vehicle.find('VehicleLongitude')
        print('lat lon are ' + str(lat) + str(lon))
    
    print("I know the data is there because I can access it")
    for vehicle in root:
        lat = vehicle[8].text
        lon = vehicle[9].text
        print('lat lon by index ' + str(lat) + str(lon))

    print("I think 'find' should work because vehicle is an ElementObject")
    for vehicle in root:
        print('vehicle type: ' + str(type(vehicle)))
        
def printXML (busNum):
    "This function takes a bus number and prints the XML location data nicely for viewing"
    locations = urllib.request.urlopen('http://svc.metrotransit.org/NexTrip/VehicleLocations/' + busNum)
    data = locations.read()

    f = open('locations.xml', 'wb')
    f.write(data)
    f.close()

    xml = MD.parse('locations.xml')
    print(xml.toprettyxml())


#bus = input('Please enter bus number or \"0\" for all: ')
bus = '444'
printXML(bus)
getlocations(bus)
