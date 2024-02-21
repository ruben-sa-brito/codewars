#https://www.codewars.com/kata/59a2a3ba5eb5d4e609000055
def find_array(arr1, arr2):
 
    return [arr1[x] for x in arr2 if len(arr1) > x]
  