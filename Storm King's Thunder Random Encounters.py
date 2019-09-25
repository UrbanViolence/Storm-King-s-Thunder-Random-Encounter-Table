import random
Y = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + 2   
n = random.randint(1, 100)
z = random.randint(1,4)
D = random.randint(2,20)
_1d2 = random.randint(1,2)
_1d3 = random.randint(1,3)
_1d4 = random.randint(1,4)
_2d4 = random.randint(1,4) + random.randint(1,4)
_1d6 = random.randint(1,6)
_2d6 = random.randint(1,6) + random.randint(1,6)
_3d6 = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
_4d6 = random.randint(1,6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1,6)
_6d6 = random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
_1d10 = random.randint(1,10)
_2d10 = random.randint(1,10) + random.randint(1,10)
_3d10 = random.randint(1,10) + random.randint(1,10) + random.randint(1,10)


PrintBandits= 'A marauding gang of bandits confronts the party. The gang consists of a bandit captain and  ' + str(Y) + ' bandits, all wearing cloaks and mounted on riding horses. They demand tribute! The captain promises not to attack in exchange for a toll (no less than 100 gp worth of treasure). If the characters pay up, the captain bids them a safe journey before departing peacefully. Each bandit carries a pouch containing ' + str(_1d10) + ' gp. The bandit captain’s pouch holds ' + str(D) + ' gp and '+ str(_1d6) + ' gems worth 100 gp each.'

PrintBarbarians= 'The characters encounter a hostile group of Uthgardt barbarians consisting of ' + str(_4d6) + ' tribal warriors and an Uthgardt shaman (appendix C).'

PrintBattlefield= 'The characters discover the corpses of ' + str(_4d6) + ' barbarians and ' + str(_1d4) +' frost giants. The barbarians and giants appear to have killed one another within the past week. Carrion birds and one or two wolves pick at the corpses and flee if they are startled or attacked'

PrintElfGuide='A band of ' + str(_3d6) + ' wood elves offers to escort the party through the forest, steering the characters around the elves’ hidden settlements. If they accept the offer, the characters have no hostile encounters while passing through the forest. If the characters refuse, the elves offer no further assistance and disappear into the woods. The elves use the scout statistics, with the following changes:The elves are chaotic good. Their speed is 35 feet, and they can attempt to hide even when they are in an area only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.They have advantage on saving throws against being charmed, and magic can’t put them to sleep.They have darkvision out to a range of 60 feet.They speak Common and Elvish.'

PrintFireGiant= 'A fire giant is searching for lost fragments of the Vonindod. The giant carries a rod of the Vonindod (see appendix B), and' + str(_1d4+2) + ' smoke mephits are fluttering around it. The giant is frustrated because weeks of searching have yielded nothing of value. If it spots the adventurers, it puts away the rod and begins hurling rocks at them to alleviate its boredom and frustration. The mephits follow the giants’ commands to the best of their ability, though they loathe melee combat. On subsequent occurrences of this encounter, you can replace the mephits with ' + str(_1d2) +' hell hounds, '+ str(_1d2) +' fire elementals, or '+ str(_1d4 + 2) + ' magmins. The fire giant has a sack containing ' + str(_2d6 * 100) +'CP' + str(_3d6 * 100) +'SP' + str(_1d6 * 100) + 'GP, and one mundane item, determined by rolling on the Items in a Giant’s Bag table in the introduction.'

PrintFoodhunter='A male hill giant is looking for food, stuffing anything that looks even remotely edible into a big sack that he drags behind him. Lagging a few hundred feet behind the giant are ' + str(_1d4) + ' bored ogres and ' + str(_1d6) +' bugbears. Characters spot the giant from far enough away that they can plan an ambush. For an ambush to succeed, the characters must catch the monsters by surprise by succeeding on a group DC 10 Dexterity (Stealth) check. The ogres and bugbears carry no treasure. The hill giant’s sack contains '+ str(_1d4) + ' mundane items, determined by rolling on the Items in a Giant’s Bag table in the introduction.'

PrintFrostGiant='The characters come upon '+ str(_1d3) + 'frost giants. If a single giant is encountered, it has a winter wolf companion. The giants are marauders looking for homesteads or caravans to wreck and plunder.'

PrintHillGiant='A band of ' + str(_1d2 + 1) +' male hill giants is searching for homesteads to pillage. The giants hurl rocks at any small folk they see. If the giants are anywhere near Grudd Haug (see chapter 5, “Den of the Hill Giants”), the characters might be able to convince a defeated, captured giant to lead them there. Each giant carries a sack holding 1d3 mundane items; roll on the Items in a Giant’s Bag table in the introduction to determine the contents of each one.'

PrintHorseWagon='The characters encounter a draft horse pulling a batterd old wagon. Accompanying the wagon are ' +str(_1d6 - 1) + 'people (use the commoner stat block unless otherwise noted) If no commoners are present, that means the drivers are either missing or dead, leaving the horse and wagon unattended. If one or more people are present, assume they are guiding the wagon towards the nearest settlement. The encounter might be one of the following. 1. Friendly furriers transporting' + str(_2d4)+' bundles of animal pelts worth 50gp each. 2. Friendly peddlers transporting ' + str(_3d6) + ' ten gallon kegs of dwarven ale worth 5gp each. 3. Friendly, dirt-poor musicians looking for a tavern or an inn; the wagon holds their instruments, food, and traveling gear. 4.Hostile bandits (NE male and female Illuskan humans) posing as friendly traders, transporting a stolen wagon laden with foodstuffs to their encampment. 5 A family fleeing their homestead in the wake of rumors of giant sightings; the wagon contains their food and their mundane belongings. 6 A friendly merchant transporting ' + str(_2d4) +'  pigs worth 3 gp each; any other persons present are Zhentarim guards (N male and female humans of various ethnicities) hired to ward off bandits and other threats. 7Friendly Zhentarim mercenaries (NG male and female human veterans of various ethnicities) transporting thirty longswords (worth 15 gp each) and fifty shortswords (worth 10 gp each) to a Zhent merchant waiting for them in the nearest settlement.'

PrintKnight='The Order of the Gauntlet is taking strides to deal with the giant threat. The characters encounter a knight of the order mounted on a warhorse clad in chain mail barding (AC 16).'

PrintOgres='The characters hear loud, deep voices and spot ' + str(_1d4 + 1) + ' ogres from a safe distance away. The big dummies are lost and trying to find their way home, whether that is Grudd Haug (see chapter 5, “Den of the Hill Giants”) or some other location. The characters catch them in the middle of a loud argument about which direction they should go, and can easily avoid the ogres or take them by surprise. The ogres have no treasure.'

PrintOrcs= 'The characters come across ' + str(_3d6 + 2) + ' orcs.'

PrintTravelersGrassland= 'The party encounters ' + str(_1d6) + 'farmers whose homestead was attacked by hill giants, or ' +str(_1d4) + ' ranchers on riding horses who are heading to a nearby settlement to warn it about giants in the area.'

PrintTravelersHills= 'The party encounters ' + str(_1d4) + ' shepherds guiding the remnants of their flock to safety after a harrowing hill giant encounter.'

PrintTravelersMountaints= ' The party encounters ' + str(_1d4) + ' prospectors or miners who had a close call with some frost giants or stone giants and were forced to leave behind their mining gear and supplies, and treasure.'

PrintTravelersRoad= 'The party encounters either' +str(_3d6) + 'peasants fleeing their homes after a frost giant, hill giant, or stone giant attack; an angry mob of ' +str(_6d6) + ' peasants looking to reclaim their land or avenge dead loved ones or a lone merchant or minstrel in a horse-drawn wagon who is relocating to a safer settlement.'

PrintTravelersSea= 'The party encounters either a friendly vessel carrying ' +str(_6d6) + ' crew and passengers who saw a cloud giant castle or a frost giant greatship, or ' +str(_1d4) + ' survivors floating on debris after their ship was sunk by a frost giant greatship.'

PrintTravelersTundra= 'The party encounters ' +str(_1d4) + 'hunters or trappers who narrowly escaped from a fire giant or a frost giant but were forced to leave a companion behind.'

PrintOrcPrisoners= 'The prisoners are ' + str(_1d4 + 2) +' strongheart halfling commoners belonging to the Woodhew clan. The oldest among them is a feisty old gardener named Ollie Woodhew. The orcs set fire to the Woodhew homestead and captured these family members as they tried to flee. One of the orcs even broke Ollie’s favorite walking stick. If the characters escort the Woodhews back to their torched homestead, the halflings are reunited with the members of their family who avoided capture. One of them rewards the party with a family heirloom (a magic item) hidden in the burnt remains of the family home. Roll on Magic Item Table F in chapter 7 of the Dungeon Master’s Guide to determine the item.'

PrintRangers= 'The characters encounter a helpful ranger, who might be a member of the Emerald Enclave or simply a wanderer of the wilderness. Example: Saarvin (CN male dragonborn scout) travels on foot and carries his own gear. He was born in Fireshear and is the self-proclaimed King of the Frozenfar. He claims to have climbed the tallest peak in the Spine of the World and plucked coins from the hoard of a white dragon sleeping less than 10 feet away. Each night, while sitting by the campfire, he carves a tiny wooden figurine depicting one of the characters and gives it to that individual as a gift the next morning.'

PrintRangerandcompanion= 'The characters encounter a helpful ranger, who might be a member of the Emerald Enclave or simply a wanderer of the wilderness. They have some sort of mount and some sort of animal companion. Example: Vordana Jezral (NG female lightfoot halfling scout) has the psionic ability to cast the misty step spell once per day. She is familiar with the roads and trails of the North and the settlements along them. She knows every innkeeper from Neverwinter to Deadsnows, and she has two traveling companions: a tressym (see appendix C) named Flycatcher and an old mule named Tod, which she freed from an abusive owner.'

PrintTravelersForest='The characters encounter' + str(_1d6) + ' hunters or trappers who heard something big moving through the forest and ran.'

PrintCloudCastle='The characters spot a giant castle in the clouds. The castle is drifting a mile above the ground and poses no imminent threat. If this encounter occurs anywhere near the Evermoors, the castle belongs to an evil cloud giant named Countess Sansuri (see chapter 9, “Castle of the Cloud Giants”). Otherwise, the castle is home to ' + str(_1d6 ) +' neutral good cloud giants who are searching for ancient ruins built by their ancestors. By finding and rebuilding these ancient sites, the giants hope to please their gods and help cloud giants rise to the top of the ordning. These aloof giants have no interest in helping small folk and prefer to be left alone.'

PrintCragCats= 'A group of ' +str(_1d4 + 1) + ' adult crag cats (see appendix C) hide and attempt to surprise the party. Due to their natural camouflage, the cats have advantage on their dexterity (Stealth) checks.'

PrintStoneGiants= 'A group of ' +str(_1d3) + ' stone giants is searching for settlements to destroy and ruins to dismantle. The giants might already be in the midst of dismantling a ruin, intent on wiping its existence from the face of the world. They hurl rocks at any "small folk" they see. Treasure: each giant has a sack containting ' + str(_2d6 * 100) + ' gp, ' +str(_1d6) + ' 100 gp gems, and one mundane item.'

PrintSquire='The knight has a squire — a guard mounted on an unarmored warhorse'

PrintDragon= 'The characters spot a young copper dragon flying lazy circles over its domain. Adventurers who get the dragon’s attention might be able to bribe it in exchange for a small favor. A sample copper dragon is described below.  Vexilanthus doesn’t consider the party a threat unless they attack him. If the characters mention that they’re on the lookout for giants, Vexilanthus says that he spotted a hill giant prowling around an old tower in the hills. The dragon steers the adventurers in that direction, hoping that they’ll dispose of the giant. If the characters take the bait, see the "old tower" section at the end of the chapter. For a payment of 500 gp or more, Vexilanthus wil provide safe escort to the nearest settlement.'

PrintSeaFrostGiants= 'The party encounters a frost giant greatship (see chapter 7 "Berg of the Frost Giants") with twenty hostile frost giants aboard. If the characters are traveling aboard a vessel that has a speed of at least 3 miles per hour, their ship can outpace the frost giants greatship. Otherwise, the greatship overtakes them. Treasure: Each frost giant has a sack containing ' + str(_3d6*100)  + ' cp, ' + str(_2d6*100) + ' sp, ' + str(_1d6*100) + ' gp, and one mundane item determined by rolling on the mundane items table.'

PrintSeaBarbarians= ' The characters encounter ' + str(_1d3) + ' longships, each with ten beserkers and thirty tribal warriors aboard. One of the beserkers serves as the captain. These hostile, bloodthirsy Northfolk raiders hail from Gundarlun, the Korinn Archipelago, Tuern, or the Whalebones. The longships have a speed of three miles per hour. If the vessel the characters are in moves at least as fast, the characters can flee from the barbarians and avoid an altercation.'

PrintElk='The characters come across a herd of ' + str(_2d10) + ' elk. They are not hostile and flee if attacked.' 

PrintSeaOgres= 'The party encounters ' +str(_1d4 + 1) + ' merrow. The merrow try to harpoon characters and pull them into the water.' 

PrintSeaElves= 'The characters encounter ' + str(_3d6) + ' friendly sea elves. These elves know the location of Maelstrom (see chapter 10, "Hold of the Storm Giants") and can lead the characters there upon request; they also warn characters about Maelstroms whirlpool if they are headed in that direction. Sea elves use the merfolk statistics, with the following changes: They are elves, they are chaotic good, they have advantage on saving throws against being charmed, magic can not put them to sleep, they have darkvision, and they can speak common and elvish.'

PrintSeasBandits= 'The characters encounter a pirate captain (use the bandit captain stat block) and twenty pirates (use the bandit stat block) on a longship. Longships have a The longships have a speed of three miles per hour. If the vessel the characters are in moves at least as fast, the characters can flee from the pirates. Otherwise, the pirates overtake the characters vessel and board it, threatening to kill everyone aboard unless the characters surrender the contents of their ships hold. If the characters comply with the pirates demands, the pirates transfer the cargo and flee with their booty. Treasure: Each bandit carries a pouch containing ' + str(_1d10) + ' gp. The bandit captains pouch holds ' + str(_2d10) + 'gp and ' + str(_1d6) + ' gems worth 100 gp each.'

PrintDigsite = 'A fire giant equipped with a rod of the Vonindod (see appendix B) has located a particularly large fragment of the Vonindod and has tasked its minions with digging it up. The giant oversees ' +str(_1d4 + 1) + ' ogres, ' + str(_2d6 + 2) +' hobgoblins, ' + str(_2d6 + 10) +' goblins. The ogres are using ropes to pull the 2,000-pound fragment out of a 50-foot-wide, 30-foot-deep crater. The hobgoblins scream at the ogres to put their backs into it. The goblins lie around the outskirts of the crater, picks and shovels scattered between them. The goblins have spent the past several days digging the crater and are suffering from five levels of exhaustion (see appendix A in the Player’s Handbook).'

PrintBeserkers= ' berserkers and a tribal chieftain (a beserker with 90 hp) also appear. '

print('Are you in the Forest, Grassland, Hills, Mountains, Road, Sea, or Tundra?')
L = input()
if L == ('Forest'):
    print(n)
    if (n >= 1) and (n <= 8):
         print(PrintBandits)
    elif (n >= 9) and (n <= 18):
        print(PrintBarbarians)
        if (_4d6 >= 20): print( str(_1d3) + PrintBeserkers)
    elif (n>= 19) and (n <= 21):
        print(PrintBattlefield)
    elif (n>= 22) and (n <= 29):
        print(PrintDigsite)
    elif (n>= 30) and (n <= 37):
        print(PrintElk)
    elif (n>= 38) and (n <= 53):
        print(PrintElfGuide)
    elif (n>= 54) and (n <= 55):
        print(PrintFireGiant)
    elif (n>= 56) and (n <= 62):
        print(PrintFoodhunter)
    elif (n>= 63) and (n <= 67):
        print(PrintFrostGiant)
    elif (n>= 68) and (n <= 70):
        print(PrintHillGiant)
    elif (n>= 71) and (n <= 75):
        print(PrintHorseWagon)
    elif (n>= 76) and (n <= 80) and (_1d2 ==2):
        print(PrintKnight)
        if (n>= 76) and (n <= 80) and (_1d2 == 1):
            print(PrintSquire)     
    elif (n >= 81) and (n <= 82):
        print(PrintOgres)
    elif (n >= 83) and (n <= 90):
        print(PrintOrcs)
        if (_1d4 == 4):
            print(PrintOrcPrisoners)
    elif (n >= 91) and (n <= 95) and (animalcompanion == 1):
        print(PrintRangers)
    elif (n >= 91) and (n <= 95) and (animalcompanion == 2):
        print(PrintRangerandcompanion)
    elif (n >= 96) and (n <= 100):
        print(PrintTravelers)
    

if L == 'Grassland':
    print(n)
    if (n >= 1) and (n <= 7):
        print(PrintBandits)
    elif (n >= 8) and (n <= 32):
        print(PrintBarbarians)
        if (_4d6 >= 20): print( str(_1d3) + PrintBeserkers) 
    elif (n >= 33) and (n <= 37):
        print(PrintBattlefield)
    elif (n >= 38) and (n <= 39):
        print(PrintCloudCastle)
    elif (n >= 40) and (n <= 46):
        print(PrintDigsite)
    elif (n >= 47) and (n <= 53):
        print(PrintElk)
    elif (n >= 54) and (n <= 55):
        print(PrintFireGiant)
    elif (n >= 56) and (n <= 62):
        print(PrintFoodhunter)
    elif (n >= 63) and (n <= 66):
        print(PrintFrostGiant)
    elif (n >= 67) and (n <= 68):
        print(PrintHillGiant)
    elif (n >= 69) and (n <= 75):
        print(PrintHorseWagon)
    elif (n>= 76) and (n <= 80) and (_1d2 ==2):
        print(PrintKnight)
        if (n>= 76) and (n <= 80) and (_1d2 == 1):
            print(PrintSquire)         
    elif (n >= 79) and (n <= 84):
        print(PrintOgres)
    elif (n >= 83) and (n <= 90):
        print(PrintOrcs)
        if (_1d4 == 4):
            print(PrintOrcPrisoners)
    elif (n >= 91) and (n <= 95) and (animalcompanion == 1):
        print(PrintRangers)
    elif (n >= 91) and (n <= 95) and (animalcompanion == 2):
        print(PrintRangerandcompanion)
    elif (n >= 96) and (n <= 100):
        print(PrintTravelersGrassland)
    
if L == ('Hills'):
    print(n)
    if (n >=1) and (n <= 4):
        print(PrintBandits)
    elif (n >= 5) and (n <= 24):
            print(PrintBarbarians)
            if (_4d6 >= 20): print( str(_1d3) + PrintBeserkers) 
    elif (n >= 25) and (n <= 28):
        print(PrintBattlefield)
    elif (n >= 29) and (n <= 30):
        print(PrintCloudCastle)
    elif (n >= 31) and (n <= 35):
        print(PrintCragCats)
    elif (n >= 36) and (n <= 38):
        print(PrintDigsite)
    elif (n >= 39) and (n <= 41):
        print(PrintDragon)
    elif (n >= 42) and (n <= 50):
        print(PrintElk)
    elif (n >= 51) and (n <= 53):
        print(PrintFireGiant)
    elif (n >= 54) and (n <= 59):
        print(PrintFoodhunter)
    elif (n >= 60) and (n <= 61):
        print(PrintFrostGiant)
    elif (n >= 62) and (n <= 76):
        print(PrintHillGiant)
    elif (n>= 77) and (n <= 80) and (_1d2 ==2):
        print(PrintKnight)
        if (_1d2 == 1): print(PrintSquire)
    elif (n >= 81) and (n <= 85):
        print(PrintOgres)
    elif (n >= 86) and (n <= 90):
        print(PrintOrcs)
        if (_1d4 == 4): print(PrintOrcPrisoners)
    elif (n >= 91) and (n <= 94) and (animalcompanion == 1):
        print(PrintRangers)
    elif (n >= 91) and (n <= 94) and (animalcompanion == 2):
        print(PrintRangerandcompanion)
    elif (n >= 95) and (n <= 97):
        print(PrintStoneGiants)
    elif (n >= 98) and (n <= 100):
        print(PrintTravelersHills)

if L == ('Mountains'):
    print(n)
    if (n >= 1) and (n <= 10):
        print(PrintBarbarians)
        if (_4d6 >= 20): print( str(_1d3) + PrintBeserkers) 
    elif (n>=11) and (n <= 15):
        print(PrintCloudCastle)
    elif (n>=16) and (n <= 32):
        print(PrintCragCats)
    elif (n>=33) and (n <= 35):
        print(PrintDigsite)
    elif (n>=36) and (n <= 43):
        print(PrintElk)
    elif (n>=44) and (n <=49 ):
        print(PrintFireGiant)
    elif (n>=50) and (n <= 52):
        print(PrintFoodhunter)
    elif (n>=53) and (n <= 60):
        print(PrintFrostGiant)
    elif (n>=61) and (n <= 62):
        print(PrintHillGiant)
    elif (n>= 63) and (n <= 74) and (_1d2 ==2):
        print(PrintKnight)
        if (n>= 63) and (n <= 74) and (_1d2 == 1):
            print(PrintSquire) 
    elif (n>=65) and (n <= 66):
        print(PrintOgres)
    elif (n >= 67) and (n <= 79):
        print(PrintOrcs)
        if (_1d4 == 4): print(PrintOrcPrisoners)
                
    elif (n >= 80) and (n <= 83) and (animalcompanion == 1):
        print(PrintRangers)
    elif (n >= 80) and (n <= 83) and (animalcompanion == 2):
        print(PrintRangerandcompanion)
    elif (n>=84) and (n <= 95):
        print(PrintStoneGiants)
    elif (n>=96) and (n <= 100):
        print(PrintTravelersMountaints)

if L == ('Road'):
    print(n)
    if (n>= 1) and (n <= 8):
        print(PrintBandits)
    elif (n>= 9) and (n <= 13):
         print(PrintCragCats)
    elif (n>= 14) and (n <= 20):
        print(PrintDragon)
    elif (n>= 21) and (n <= 28):
        print(PrintFireGiant)
    elif (n>= 29) and (n <= 37):
        print(PrintFoodhunter)
    elif (n>= 38) and (n <= 41):
        print(PrintFrostGiant)
    elif (n>= 42) and (n <= 46):
        print(PrintHillGiant)
    elif (n>= 47) and (n <= 55):
        print(PrintHorseWagon)
    elif (n>= 56) and (n <= 64) and (_1d2 ==2):
        print(PrintKnight)
        if (n>= 56) and (n <= 64) and (_1d2 == 1):
            print(PrintSquire)
    elif (n>= 65) and (n <= 69):
        print(PrintOgres)
    elif (n >= 70) and (n <= 73):
        print(PrintOrcs)
        if (_1d4 == 4):
            print(PrintOrcPrisoners)
    elif (n >= 74) and (n <= 78) and (animalcompanion == 1):
        print(PrintRangers)
    elif (n >= 74) and (n <= 78) and (animalcompanion == 2):
        print(PrintRangerandcompanion)
    elif (n>= 79) and (n <= 80):
        print(PrintStoneGiants)
    elif (n>= 81) and (n <= 100):
        print(PrintTravelersRoad)
    
if L == ('Sea'):
    print(n)
    if (n>= 1) and (n <= 20):
        print(PrintSeasBandits)
    elif (n >= 21) and (n <= 40):
        print(PrintSeaBarbarians)
    elif (n>= 41) and (n <= 50):
        print(PrintSeaElves)
    elif (n>= 51) and (n <= 70):
        print(PrintSeaFrostGiants)
    elif (n>= 71) and (n <= 80):
        print(PrintSeaOgres)
    elif (n>= 81) and (n <= 100):
        print(PrintTravelersSea)

if L == ('Tundra'):
    print(n)
    if (n >= 1) and (n <= 15):
        print(PrintBarbarians)
        if (_4d6 >= 20): print( str(_1d3) + PrintBeserkers) 
    elif (n>= 16) and (n <= 19):
        print(PrintBattlefield)
    elif (n>= 20) and (n <= 22):
        print(PrintCloudCastle)
    elif (n>= 23) and (n <= 35):
        print(PrintCragCats)
    elif (n>= 36) and (n <= 41):
        print(PrintDigsite)
    elif (n>= 42) and (n <= 54):
        print(PrintElk)
    elif (n>= 55) and (n <= 56):
        print(PrintFireGiant)
    elif (n>= 57) and (n <= 58):
        print(PrintFoodhunter)
    elif (n>= 59) and (n <= 70):
        print(PrintFrostGiant)
    elif (n>= 71) and (n <= 74):
        print(PrintHillGiant)
    elif (n>= 75) and (n <= 76):
        print(PrintOgres)
    elif (n >= 77) and (n <= 87):
        print(PrintOrcs)
        if (_1d4 == 4):
            print(PrintOrcPrisoners)
    elif (n >= 88) and (n <= 93) and (animalcompanion == 1):
        print(PrintRangers)
    elif (n >= 88) and (n <= 93) and (animalcompanion == 2):
        print(PrintRangerandcompanion)
    elif (n>= 94) and (n <= 95):
        print(PrintStoneGiants)
    elif (n>= 96) and (n <= 100):
        print(PrintTravelersTundra)
    



        




















