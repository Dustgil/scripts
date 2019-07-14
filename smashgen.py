import random

'''
List of all Smash 5 characters in the order they appear on the select fighter screen.
The order is left-to-right. If you don't have a character, make sure to exclude that character.

0    Mario
1    Donkey Kong
2    Link
3    Samus
4    Dark Samus
5    Yoshi
6    Kirby
7    Fox
8    Pikachu
9    Luigi
10    Ness
11   Captain Falcon
12   Jigglypuff
13   Peach
14   Daisy
15   Bowser
16   Ice Climbers
17   Sheik
18   Zelda
19   Dr. Mario
20   Pichu
21   Falco
22   Marth
23   Lucina
24   Young Link
25   Ganondorf
26   Mewtwo
27   Roy
28   Chrom
29   Mr. Game & Watch
30   Pit
31   Meta Knight
32   Dark Pit
33   Zero Suit Samus
34   Wario
35   Snake
36   Ike
37   Pokemon Trainer
38   Diddy Kong
39   Lucas
40   Sonic
41   King Dedede
42   Olimar
43   Lucario
44   R.O.B.
45   Toon Link
46   Wolf
47   Villager
48   Mega Man
49   Wii Fit Trainer
50   Rosalina & Luma
51   Little Mac
52   Greninja
53   Palutena
54   Pac-Man
55   Robin
56   Shulk
57   Bowser Jr.
58   Duck Hunt
59   Ryu
60   Ken
61   Cloud
62   Corrin
63   Bayonetta
64   Inkling
65   Ridley
66   Simon
67   Richter
68   King K. Rool
69   Isabelle
70   Incineroar
71   Piranha Plant
'''

character_list_true = [
    'Mario',
    'Donkey Kong',
    'Link',
    'Samus',
    'Dark Samus',
    'Yoshi',
    'Kirby',
    'Fox',
    'Pikachu',
    'Luigi',
    'Ness',
    'Captain Falcon',
    'Jigglypuff',
    'Peach',
    'Daisy',
    'Bowser',
    'Ice Climbers',
    'Sheik',
    'Zelda',
    'Dr. Mario',
    'Pichu',
    'Falco',
    'Marth',
    'Lucina',
    'Young Link',
    'Ganondorf',
    'Mewtwo',
    'Roy',
    'Chrom',
    'Mr. Game & Watch',
    'Meta Knight',
    'Pit',
    'Dark Pit',
    'Zero Suit Samus',
    'Wario',
    'Snake',
    'Ike',
    'Pokemon Trainer',
    'Diddy Kong',
    'Lucas',
    'Sonic',
    'King Dedede',
    'Olimar',
    'Lucario',
    'R.O.B.',
    'Toon Link',
    'Wolf',
    'Villager',
    'Mega Man',
    'Wii Fit Trainer',
    'Rosalina & Luma',
    'Little Mac',
    'Greninja',
    'Palutena',
    'Pac-Man',
    'Robin',
    'Shulk',
    'Bowser Jr.',
    'Duck Hunt',
    'Ryu',
    'Ken',
    'Cloud',
    'Corrin',
    'Bayonetta',
    'Inkling',
    'Ridley',
    'Simon',
    'Richter',
    'King K. Rool',
    'Isabelle',
    'Incineroar',
    'Piranha Plant'
    ]
character_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24, \
                  25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46, \
                  47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71]

# don't touch the next three variables.
profile_list = []
names = []
modes = []

p1 = [71,20,46,49,51,59,60,70,26,63,65,38]
p1name = "coton"
p1mode = 0 # 0 for exclusive, 1 for inclusive.


profile_list.append(p1) # comment these out if profile not used
names.append(p1name)
modes.append(p1mode)


p2 = [71,59,60,67,25]
p2name = "Nick"
p2mode = 0


profile_list.append(p2) # comment these out if profile not used. to use, these must be uncommented.
names.append(p2name)
modes.append(p2mode)

p3 = [71,12,20,42,10,7,17,49,43]
p3name = "1"
p3mode = 0

profile_list.append(p3) # comment these out if profile not used. to use, these must be uncommented.
names.append(p3name)
modes.append(p3mode)

p4 = [1,2,3,4,5,6,7]
p4name = "sample"
p4mode = 1

#profile_list.append(p4) # comment these out if profile not used. to use, these must be uncommented.
#names.append(p4name)
#modes.append(p4mode)




# this is the end of the settings. everything else shouldn't be touched unless you know what you're doing.



def select(profile, mode):
    if mode == 0: # setup exclusive loop. loops through until a number is
                  # generated that does not match any in the profile.
        
        set = 0
        while set == 0:
            set = 1 # immediately sets to 1. if the generated number is in the
                    # profile, set back to 0 and the while loop is forced to repeat.
            n = random.randint(0, len(character_list) - 1)
            for e in profile:
                if e == n:
                    set = 0
        print(character_list_true[n])

    if mode == 1: # setup inclusive loop.
        n = random.randint(0, len(profile) - 1)
        print(character_list_true[profile[n]])

                

# now generate character for each person, using a counter to iterate through
# the name and mode lists

counter = 0
for e in profile_list:
    print(names[counter])
    select(e, modes[counter])
    counter += 1

