#https://www.codewars.com/kata/5f8341f6d030dc002a69d7e4
def least_larger(a, i)
  
    num = a.index((a.filter {|num| num > a[i]}).min)
    num == nil ? -1 : num
    
end