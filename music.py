import sys
import xml.etree.ElementTree as ET

alters = {'-1': 'flat', '0': 'natural', '1': 'sharp'}

input_file = sys.argv[1]
print "Importing %s" % input_file
root = ET.parse(input_file).getroot()
for measure in root.iter('measure'):
   print("Bar %s" % measure.get('number'))
   for note in measure.iter('note'):
     pitch = note.find('pitch')
     step = pitch.find('step').text
     alter = alters.get(pitch.find('alter').text, 'unknown alteration')
     octave = pitch.find('octave').text

     duration = note.find('type').text
     if (note.find('dot') is not None):
       duration = "dotted %s" % duration

     print "%s%s %s %s" % (step, octave, alter, duration)
