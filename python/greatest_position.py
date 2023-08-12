#https://www.codewars.com/kata/5442e4fc7fc447653a0000d5
def greatest_distance(arr):
    distance = 0
    index1 = 0
    for num in arr:
        index2 = 0
        for num2 in arr:
            if num == num2:
                
                dst = abs(index1 - index2)
                if dst > distance:
                    distance = dst
            index2 += 1        
        index1 += 1            
    
    return distance               