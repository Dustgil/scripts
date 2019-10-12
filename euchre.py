import random
cards = ['As','Ks','Qs','Js','10s','9s',
         'Ac','Kc','Qc','Jc','10c','9c',
          'Ad','Kd','Qd','Jd','10d','9d',
          'Ah','Kh','Qh','Jh','10h','9h']
suits = {'spades': ['As','Ks','Qs','Js','10s','9s'],
         'clubs': ['Ac','Kc','Qc','Jc','10c','9c'],
         'diamonds': ['Ad','Kd','Qd','Jd','10d','9d'],
         'hearts': ['Ah','Kh','Qh','Jh','10h','9h']
         }

def determine_winner(tru, lead, played_cards):
    # construct a list of card rankings and give trick to highest card holder
    # only need to construct list of trump cards and leading card suit as
    # these will be the highest ranking cards and one of them must be played.

    ranking = []
    if tru == 'spades':
        ranking.append(suits[tru][3])
        ranking.append(suits['clubs'][3])
        for card in suits[tru]:
            ranking.append(card) # can append jack twice because it wont affect ranking, less computationally expensive.
        for card in suits[lead]:
            ranking.append(card)

    if tru == 'clubs':
        ranking.append(suits[tru][3])
        ranking.append(suits['spades'][3])
        for card in suits[tru]:
            ranking.append(card) # can append jack twice because it wont affect ranking, less computationally expensive.
        for card in suits[lead]:
            ranking.append(card)

    if tru == 'diamonds':
        ranking.append(suits[tru][3])
        ranking.append(suits['hearts'][3])
        for card in suits[tru]:
            ranking.append(card) # can append jack twice because it wont affect ranking, less computationally expensive.
        for card in suits[lead]:
            ranking.append(card)

    if tru == 'hearts':
        ranking.append(suits[tru][3])
        ranking.append(suits['diamonds'][3])
        for card in suits[tru]:
            ranking.append(card) # can append jack twice because it wont affect ranking, less computationally expensive.
        for card in suits[lead]:
            ranking.append(card)


        # now iterate through rankings, and check if each card is in list
        # return index for first card to show up. thats the trick winner.

    print(ranking)

    for i in ranking:
        if i in played_cards:
            return played_cards.index(i)
                

print(determine_winner('clubs', 'diamonds', ['Kd','10d','9s','10c']))
    
    
    
    
    
                
    

p1p3_score = 0
p2p4_score = 0

player_list = [1,2,3,4]
dealer = player_list[0]

while p1p3_score < 10 & p2p4_score < 10:
    

    random.shuffle(cards)

    p1_hand = cards[0:5]
    p2_hand = cards[5:10]
    p3_hand = cards[10:15]
    p4_hand = cards[15:20]
    print(p1_hand)

    flip_up = cards[20]
    print(flip_up)

    

