#https://www.codewars.com/kata/53dc54212259ed3d4f00071c
def sum(numbers)
  if numbers == []
    return  0
  end
  numbers.inject(:+)
end
