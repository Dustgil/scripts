import random
cards = ['As','Ks','Qs','Js','10s','9s',
         'Ac','Kc','Qc','Jc','10c','9c',
          'Ad','Kd','Qd','Jd','10d','9d',
          'Ah','Kh','Qh','Jh','10h','9h']

p1p3_score = 0
p2p4_score = 0

player_list = [1,2,3,4]
dealer = player_list[0]

while p1p3_score < 10 && p2p4_score < 10:
    

    random.shuffle(cards)

    p1_hand = cards[0:5]
    p2_hand = cards[5:10]
    p3_hand = cards[10:15]
    p4_hand = cards[15:20]
    print(p1_hand)

    flip_up = cards[20]
    print(flip_up)

    

