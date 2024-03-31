#https://www.codewars.com/kata/5a1c28f9c9fc0ef2e900013b
def pyramid(n)
  return "/\\\n" if n == 1

  pyramid = ""

  n.times do |x|
    pyramid += " "*(n-x-1) + "/" + "\\\n" if x == 0
    pyramid += " "*(n-x-1) + "/" + " "*(x+(1*x)) + "\\\n" if x != 0 and x < n-1
    pyramid += " "*(n-x-1) + "/" + "_"*(x+(1*x)) + "\\\n" if x == n-1
  end

  pyramid

end
