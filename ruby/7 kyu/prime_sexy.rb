#https://www.codewars.com/kata/56b58d11e3a3a7cade000792
require 'prime'
def sexy_prime(x, y)
    return false if x == 1 || y == 1 || (x - y).abs != 6     
    Prime.prime?(x) and Prime.prime?(y)
end