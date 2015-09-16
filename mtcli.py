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

print("\nfor elem in iter on tree")
iter_ = tree.getiterator()
for elem in iter_:
    print(elem.tag)

appointments = root.getchildren()
print ("\nfor child in children on tree.getchildren()")
for appointment in appointments:
    appt_children = appointment.getchildren()
    for appt_child in appt_children:
        print(appt_child.tag, appt_child.text)

stops = urllib.request.urlopen('http://svc.metrotransit.org/NexTrip/Stops/' + busNum + '/2')
data = stops.read()
f = open('stops.xml', 'wb')
f.write(data)
f.close()

tree = ET.parse('stops.xml')
root = tree.getroot()

