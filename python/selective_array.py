#https://www.codewars.com/kata/58f6000bc0ec6451960000fd

def sel_reverse(arr,l):
    
    if l == 0: return arr
    
    arr.append('end')
    
    cut = [arr[arr.index(x) - l: arr.index(x)] for x in arr if arr.index(x)%l == 0 and x != arr[0]]
    
    arr.remove('end')
    
    if len(arr) % l != 0:
        rest = arr[(len(arr)%l)*-1:]
        rest.reverse()
        return [num for ls in cut for num in reversed(ls)] + rest
    return [num for ls in cut for num in reversed(ls)]