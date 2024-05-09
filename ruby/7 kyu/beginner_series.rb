#https://www.codewars.com/kata/55f2b110f61eb01779000053
def get_sum(a,b)
    return (a..b).to_a.sum if a <= b
    (b..a).to_a.sum 
end