#!/usr/bin/python

import sys
import zlib
import xml.etree.ElementTree as ET

messages = {
8640: '"A ladder, Master." / "That ladder will see us to the roof."',
8641: '"An armorer, I believe." / "We\'re like to have dealings with the armorer here for some time to come." / "Also, some weapons can be further enhanced with their aid." / "Have you aught to sell?" / "Have you equipment to enhance?" / "All these workers going about their business... How lively."',
8642: '"\'Tis not the last we\'ll call upon this inn, I\'ll warrant." / "Aye, the inn offers a clean bed, but it deals in vocations and skills, besides." / "Ought we adjust our inventory?"',
8643: '"This inn can serve as the hub of our journeys." / "Here we can rest, manage inventory and skills, and so on." / "Remember to save enough for lodging." / "Are your travel preparations complete?" / "I\'d imagine one would never tire of this place."',
8644: '"What meaning do you suppose those stones hold?" / "\'Tis a portcrystal. With a ferrystone, you could reach it from anywhere." / "\'Tis a Portcrystal, Master."',
8645: '"Some corners of the capital can only be reached by crossing the rooftops."',
8646: '"This city has a church as well?" / "Gran Soren\'s cathedral is a handsome structure."',
8647: '"We can take on curatives and other supplies for our journey here." / "Armorers trade in a wide variety of weapons and defensive equipment." / "Remember to both buy and sell items regularly." / "The life of a salesman surely has its own trials." / "As expected of a residential area, \'tis much more quiet." / "A place one can live without fear of monsters!" / "\'Tis dreadfully easy to while away hours just shopping."',
8648: '"Hmm... This shop bears a rather unwholesome look to it..." / "The scrivener at The Black Cat here can duplicate objects in your possession."',
8649: '"Precious things gone lost or missing have a way of turning up there."',
8650: '"What\'s more, the proprietor can furnish forgeries of certain items."',
8651: '"Hm? \'Tis a barber\'s shop."',
8652: '"This shop will see to your hair, should you be of a mind to have it styled."',
8653: '"Even my kind enjoy a new coiffure from time to time."',
8654: '"The barber keeps abreast of the latest tonsorial trends, if you fancy a cut."'
}

for arg in sys.argv[1:]:
	f = open(arg, "rb")
	f.seek(32)
	tree = ET.fromstring(zlib.decompress(f.read()))
	f.close()
	flags = tree.find('.//array[@name="mStudyFlag"]')
	n = 270 * 32
	v = int(flags[270].get('value'))

	for i in range(32):
		if v & 1 == 0 and n in messages:
			print(messages[n])
		v >>= 1
		n += 1
	
