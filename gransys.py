#!/usr/bin/python

import sys
import zlib
import xml.etree.ElementTree as ET

messages = {
8256: '1: "\'Tis safest on the roads." / "The roads are safer than the brush, but still we\'d best stay wary."',
8257: '2: "The duke could stand to commission some new roads..."',
8258: '3: "The rocks here may hold ore." / "Perhaps we\'ll find ore among the crags that litter this place."',
8259: '4: "We can see monsters for leagues on the open shore. And they us, in turn..."',
8260: '5: "Roots of this sort of tree oft yield useful herbs and other plants."',
8261: '6: "Seems we can walk beyond the shore here. Perhaps we\'ll find aught of use."',
8262: '7: "One never knows what such forgotten corners may hold."',
8263: '8: "A cave entrance hides behind the falls."',
8264: '9: "Seems we can walk beyond the shore here. Perhaps we\'ll find aught of use."',
8265: '10: "The structure is abandoned, Arisen. Let\'s have a look for supplies within."',
8266: '11: "We could scale this slope, provided we sought out the shallowest slopes."',
8267: '12: "Keep watch for falling rocks as we walk the slopes, Master."',
8268: '13: "Where visibility is poor, we must be especially wary of attacks."',
8269: '14: "Such open areas are two-edged swords. Every monster for leagues can see us."',
8270: '15: "This is a fine place to lie in ambush, Arisen."',
8271: '16: "We\'ll likely face ambush here. Stay watchful."',
8272: '17: "Goblin packs are ruled by the strong."',
8281: '18: "It falls on us to pace ourselves on roads so open."',
8282: '19: "Perhaps we\'ll find ore among the crags that litter this place."',
8283: '20: "Cast an eye below as we cross. There may be aught beneath the bridge."',
8284: '21: "Let\'s seek out the shallows, lest we lure the Brine..."',
8285: '22: "A river... I doubt we can cross it." / "Perhaps the rocks hide trinkets swept downstream."',
8286: '23: "A long-fallen waycastle, this. Still, there may yet be aught atop the wall."',
8287: '24: "We\'ll find a vantage to fire down on our foes from atop the wall."',
8288: '25: "Seems we can walk beyond the shore here. Perhaps we\'ll find aught of use."',
8289: '26: "I\'ve come to feel more at peace when the capital is in sight."',
8290: '27: "Roots of this sort of tree oft yield useful herbs and other plants."',
8291: '28: "The crags care not whom they hide. Better it be us."',
8292: '29: "Ranged attacks serve well in wide open spaces."',
8293: '30: "If we keep to the shallows, we needn\'t get soaked through."',
8294: '31: "Tis easy to slip on an incline this steep, Master. Watch your step."',
8295: '32: "Keep watch for falling rocks as we walk the slopes, Master."',
8296: '33: "Their leader infamously abhors men. Were we all female, she\'d like speak with us."',
8297: '34: "The scene of an attack, most like. Perhaps there\'s aught to be scavenged."',
8298: '35: "There must be a ladder nearby. Let\'s draw a lantern and have a look."',
8299: '36: "\'Tis a lever up above controls the gate."',
8300: '37: "I hear animals nearby. Meat would be a welcome addition to our provisions."',
8301: '38: "A lantern will draw attention out here. Stay watchful."',
8302: '39: "Every beast has its weakness. Observe closely, and learn to exploit it."',
8303: '40: "If victory is elusive, seek new allies. Where that fails, seek new foes."',
8304: '41: "Monsters fearsome strong prowl these byways, Master. Be careful."',
8305: '42: "No single strategy will serve every encounter. One must adapt."',
8320: '43: "This is a fine place to lie in ambush, Arisen."',
8321: '44: "Perhaps the figure serves as a beacon, to bring people of a kind together."',
8322: '45: "The heart of that grand figure may hold some secret..."',
8323: '46: "Caution, Master. Massive beasts prowl this area."',
8324: '47: "\'Tis the rear of the duke\'s manse."',
8325: '48: "We may be able to glean material from the boulders of this wood."',
8326: '49: "We\'re easily spotted out on the open plains."',
8327: '50: "It falls on us to pace ourselves on roads so open."',
8328: '51: "This is harpy territory. Keep watch on the skies."',
8329: '52: "With a running start, we can reach the far side."',
8330: '53: "Bandits can strike in the blink of an eye in places like this."',
8331: '54: "Keep watch for falling rocks as we walk the slopes, Master."',
8332: '55: "\'Tis the Bluemoon Tower, said to have stood here since time immemorial."',
8345: '56: "This fortress is meant to protect Gransys from the dragon... It does look very solid." / "\'Tis fear of monsters and the wyrm that gives rise to fortresses..."',
8346: '57: "If this path poses too great a risk, we might just as easily walk down below."',
8347: '58: "The waters of this marsh are suffused with fetor."',
8348: '59: "\'Tis a cage built to hold a human, Master. Is anyone inside?"',
8349: '60: "Seems there\'s a path atop the hill as well."',
8350: '61: "The fetor that corrupts this place at least offers unique materials for harvest."',
8351: '62: "Have you noticed the fireflies neutralize the poison of the marsh by night?"',
8352: '63: "\'Tis a heavy onus the men here bear."',
8361: '64: "What a splendid woodland, and so rich in resources."',
8362: '65: "The crags cast shadows fit to hide all manner of evil. Stay ready."',
8363: '66: "Seems we can walk beyond the shore here. Perhaps we\'ll find aught of use."',
8364: '67: "This area is likely rich in rabbit and other wild game."',
8365: '68: "\'Tis uneven footing. Watch your step!"',
8366: '69: "The goblins of this forest have a taste for human flesh."',
8367: '70: "Stay on your guard, Master. We journey through goblin territory."',
8368: '71: "I feel half a thief myself, sauntering through this place."',
8369: '72: "Pray, do not provoke them, Arisen! Let\'s first find their leader."',
8370: '73: "We can see monsters for leagues on the open shore. And they us, in turn..."'
}

for arg in sys.argv[1:]:
	f = open(arg, "rb")
	f.seek(32)
	tree = ET.fromstring(zlib.decompress(f.read()))
	f.close()
	flags = tree.find('.//array[@name="mStudyFlag"]')
	n = 258 * 32

	for i in range(258,262):
		v = int(flags[i].get('value'))

		for j in range(32):
			if v & 1 == 0 and n in messages:
				print(messages[n])
			v >>= 1
			n += 1

	
