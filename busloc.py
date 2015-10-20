#!/usr/bin/env python3
#
# A command line tool to get NextTrip information
#
# Chris Moser 09/25/2015
#


# Lets grab some sample bus data

import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import xml.dom.minidom as MD
#from geojson import MultiPoint
import geojson
#import json
import webbrowser

def getlocations (busNum):
    "This function takes a route number and writes a GeoJSON Multipoint array of vehicle locations"

    locations = urllib.request.urlopen('http://svc.metrotransit.org/NexTrip/VehicleLocations/' + busNum)
    root = ET.fromstring(locations.read())

    point_list = []

    for vehicle in root:
        point = [float(vehicle[9].text), float(vehicle[8].text)]
        point_list.append(point)

    multipoint_array = {
        "type": "MultiPoint",
        "coordinates": point_list,
        }
    
    multipointstring = geojson.dumps(multipoint_array)
    
    return(multipointstring)

def openMap (MultiPoint):
    "This funtions takes a MultiPoint GeoJSON object and opens a map of its points"

    params = urllib.parse.quote(str(MultiPoint))
    url = ("http://geojson.io/#data=data:application/json,%s" % params)
    webbrowser.open_new_tab(url)


def getlocationstest (busNum):
    "This function takes a route number and writes a GeoJSON Multipoint array of vehicle locations"

    locations = urllib.request.urlopen('http://svc.metrotransit.org/NexTrip/VehicleLocations/' + busNum)
    data = locations.read()
    root = ET.fromstring(data)

    print("This is what I think the answer should be")
    for vehicle in root:
        lat = vehicle.find('VehicleLatitude')
        lon = vehicle.find('VehicleLongitude')
        print('lat lon are ' + str(lat) + str(lon))

    print("This is a test section")
    for vehicle0 in root.iter('Route'):
        print("root.iter " + str(type(vehicle0)))
    
    for vehicle1 in root:
        data = vehicle1.find('Route')
        print("vehicle1.find " + str(type(data)))
    
    for vehicle2 in root:
        data = vehicle2.get('Route')
        print("vehicle2.get " + str(type(data)))

    for vehicle3 in root:
        data = vehicle3.findall('Route')
        print("vehicle3.findall " + str(type(data)))


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


bus = input('Please enter bus number or \"0\" for all: ')
#printXML(bus)
mp_string = getlocations(bus)
print(mp_string)

openMap(mp_string)

