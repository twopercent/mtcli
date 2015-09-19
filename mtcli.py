#!/usr/bin/python3.4
#
# A command line tool to get NextTrip information
#
# Chris Moser 09/10/2015
#


# Lets grab some sample bus data

import urllib.request
import xml.etree.ElementTree as ET

def parseDirection (busNum):
    "This function takes a bus number and returns a list of lists of directions and their direction code"

    directions = urllib.request.urlopen('http://svc.metrotransit.org/NexTrip/Directions/' + busNum)
    data = directions.read()
    f = open('directions.xml', 'wb')
    f.write(data)
    f.close()

    tree = ET.parse('directions.xml')
    root = tree.getroot()

    result = []

    for element in root:
        list = []
        list.append(element[0].text)
        list.append(element[1].text)

        result.append(list)
    return result

def parseStops (busNum, busDirec):
    "This function taks a bus number and direction code and returns a list of lists of stops and stop codes"

    stops = urllib.request.urlopen('http://svc.metrotransit.org/NexTrip/Stops/' + busNum + '/' + busDirec)
    data = stops.read()
    f = open('stops.xml', 'wb')
    f.write(data)
    f.close()

    tree = ET.parse('stops.xml')
    root = tree.getroot()

    result = []

    for element in root:
        list = []
        list.append(element[0].text)
        list.append(element[1].text)

        result.append(list)
    
    return result

def parseDepartures (busNum, busDirec, busStop):
    "This function taks a bus number, direction code, and stop code and returns a list of departures"

    departures = urllib.request.urlopen('http://svc.metrotransit.org/NexTrip/' + busNum + '/' + busDirec + '/' + busStop)
    data = departures.read()
    f = open('departures.xml', 'wb')
    f.write(data)
    f.close()

    tree = ET.parse('departures.xml')
    root = tree.getroot()

    result = []

    for element in root:
        list = []
        list.append(element[2].text)
        list.append(element[6].text)
        list.append(element[4].text)
        list.append(element[1].text)

        result.append(list)
    
    return result

bus = input("Please enter your bus number ")
busDirections = parseDirection(bus)

index = 0
print()

for item in busDirections:
    print(str(index) + ". " + str(item[0]))
    index += 1

print()

direction = input("Please enter your direction ")
directionKey = busDirections[int(direction)][1]
busStops = parseStops(bus, directionKey)

index = 0
print()

for item in busStops:
    print(str(index) + ". " + str(item[0]))
    index += 1

print()

stop = input("Plese enter your stop ")
stopKey = busStops[int(stop)][1]
busDepartures = parseDepartures(bus, directionKey, stopKey)

print()
print("Upcoming departures: \n")

for item in busDepartures:
    print(str(item[0]) + " " + str(item[1]) + " " + str(item[2]) + " " + str(item[3]))

print()


#appointments = root.getchildren()
#print ("\nfor child in children on tree.getchildren()")
#for appointment in appointments:
#    appt_children = appointment.getchildren()
#    for appt_child in appt_children:
#        print(appt_child.tag, appt_child.text)
