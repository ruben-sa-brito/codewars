#https://www.codewars.com/kata/5a97387e5ee396e70a00016d
def pofi(n)
  {0 => '1', 1 => 'i', 2 => '-1', 3 => '-i'}[n%4]
end
