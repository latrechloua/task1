Plateau= [ [True , False , False , False ] ,
                 [ False , True , True , False ] ]
def voisinsCase(Plateau, case=[0,0]):
    i= case[0]
    j= case[1]
    if i ==0:
        left = -1
    else:
        left = Plateau[i-1][j]
        if left == False :
            neighbor = i-1,j
    if i == len(Plateau) - 1:
        right = -1
    else:
        right = Plateau[i+1][j]
        if right == False :
            neighbor = i+1,j
    if j ==0: 
        up = -1
    else:
        up = Plateau[i][j-1]
        if up == False :
            neighbor = i,j-1
        
    if j == len(Plateau[1]) - 1:
        down = -1
    else:
        down = Plateau[i][j+1]
        if down == False :
            neighbor = i,j+1
    return neighbor 

    
print(voisinsCase(Plateau, [0,1]))
def voisinsCases (Plateau, cases=[[0,0],[0,0]]):
    neigh = []
    for case in cases:
           neigh.append(voisinsCase (Plateau, case))
    return neigh

print(voisinsCases(Plateau, [[0,1],[1,2]]))
def accessibles (Platean, deb):
    firstneigh = voisinsCase(Plateau,deb)
    neigh= [deb,firstneigh]
    while (firstneigh != [len(Plateau), len(Plateau[1])]):
        
        secneigh= voisinsCase(Plateau,firstneigh)
        
        N = neigh.append(secneigh)
        firstneigh = secneigh
    return N
    
print (accessibles(Plateau, [1,3]))

def chemin (Plateau, deb,fin):
    neighborsList= accessibles(Plateau,deb)
    for i in neighborList :
        if i == fin:
            break
            return True
        else:
            return False
print (chemin(Plateau, [1,3],[0,1]))


       
    
    
