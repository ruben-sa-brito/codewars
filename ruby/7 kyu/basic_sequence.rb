#https://www.codewars.com/kata/5436f26c4e3d6c40e5000282
def sum_of_n(n)
    seq = Array.new(n.abs+1) { |x| Array.new(x) {|y| y + 1}.sum }
    return seq unless n < 0
    seq.map {|x| x*-1}
end