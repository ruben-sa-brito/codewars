#https://www.codewars.com/kata/549ee8b47111a81214000941

def knight(p1, p2):

    enu = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    list_moves = ([2, 1],[2, -1],[-2, 1],[-2,-1],[1, 2], [1, -2], [-1, 2], [-1, -2])
    plays = 0
    control_origin = list()
    origin = [[enu[p1[0]], int(p1[1]) - 1]]
    destiny = [enu[p2[0]], int(p2[1]) - 1]

    while True:

        plays += 1
        for a in origin:
         
            for i in list_moves:
        
                if [a[0]+i[0], a[1]+i[1]] == destiny:
                    return plays

                elif(0<=(a[0]+i[0])<8 and 0<=(a[1]+i[1])<8):
                    control_origin.append([a[0]+i[0], a[1]+i[1]])
                    
        origin = control_origin

        control_origin = []