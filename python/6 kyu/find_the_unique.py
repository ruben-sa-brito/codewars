#https://www.codewars.com/kata/585d7d5adb20cf33cb000235
def find_uniq(arr):
    equal = float()
    partial = arr[0:3]
    for num in partial:
        if partial.count(num) > 1:
            equal = num
            break
            
    for num in set(arr):
        if num != equal: return num