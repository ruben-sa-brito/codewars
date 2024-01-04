#https://www.codewars.com/kata/5d37899a3b34c6002df273ee/train/python
def cant_beat_so_join(numbers):
    ordened = list()
    ind = len(numbers)
    while ind > 0:
        ordened.append(numbers[0])
        for num in numbers:
            if sum(num) > sum(ordened[-1]):
                ordened[-1] = num
        ind -=1        
        numbers.remove(ordened[-1] )
    return [num for sub in ordened for num in sub]   