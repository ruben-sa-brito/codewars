#https://www.codewars.com/kata/5839c48f0cf94640a20001d3

def land_perimeter(arr):

    island = list()
    island2 = list()
    position = 0
    ontheside = 0
    peri = 0
    slands_peri = 0

    for fields in arr:
        for field in fields:

            if field == 'X':
                slands_peri += 4

                if position in island2:
                    peri -= 2

                if ontheside == 1:
                    peri -= 2 

                island.append(position)
                ontheside = 1

            else:
                ontheside = 0  

            position += 1 

        position = 0           
        ontheside = 0          
        island2 = island
        island = []

    return f'Total land perimeter: {slands_peri + peri}'







   