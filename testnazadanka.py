grupa2 = ['gozdek','zając','cozart','bielecki','ciuk','paleta','nowak','hawrylewicz','wierzbicki','rakwic','rojkowski',
          'sikorski','głąbik','wolska','witek','witek','kluczka','broja','kuśmierski','ziółkowski','wyganowska','falfus',
          'kos','winkler','mazurkiewicz','mieszczok','knura','malejka','gębczyński','zastrzeżony','ukleja','zagała','ujazda',
          'sąsiedzki','smulska','sushko']

j: int = 0
grupa2 = sorted(grupa2)
for i in grupa2:
    print(str(j + 1) + ". " + i)
    j += 1

