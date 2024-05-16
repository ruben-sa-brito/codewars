#https://www.codewars.com/kata/588854201361435f5e0000bd
def array_conversion(arr)
    ops = ["+", "*"].cycle
    while arr.length > 1
        op = ops.next
        arr = arr.each_slice(2).map {|a, b| eval("a #{op} b")}     
    end 
    arr  
end