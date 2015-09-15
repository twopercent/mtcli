#!/usr/bin/python3.4
#
# A command line tool to get NextTrip information
#
# Chris Moser 09/10/2015
#


# Lets grab some sample bus data

import urllib.request
import xml.etree.ElementTree as ET

busNum = input("Please enter your bus number ")

directions = urllib.request.urlopen('http://svc.metrotransit.org/NexTrip/Directions/' + busNum)
data = directions.read()
f = open('directions.xml', 'wb')
f.write(data)
f.close()

print("\nYou chose bus number " + busNum)

tree = ET.parse('directions.xml')
root = tree.getroot()

print("\nNow for child in root, print child.tag and child.attrib")
for child in root:
    print (child.tag, child.attrib)

print(root[0][0].text)
print(root[0][1].text)
print(root[1][0].text)
print(root[1][1].text)

stops = urllib.request.urlopen('http://svc.metrotransit.org/NexTrip/Stops/' + busNum + '/2')
data = stops.read()
f = open('stops.xml', 'wb')
f.write(data)
f.close()

tree = ET.parse('stops.xml')
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)

print(root[0][0].text)
print(root[0][1].text)
print(root[1][0].text)
print(root[1][1].text)
