poss=[]
for j in range(3):
    tmp=[(i,j) for i in range(3)]
    poss.append(tmp)
for i in range(3):
    tmp=[(i,j) for j in range(3)]
    poss.append(tmp)
poss.extend([[(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]])
for el in poss:
    print(el)