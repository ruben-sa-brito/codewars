#https://www.codewars.com/kata/58c218efd8d3cad11c0000ef
def bin_str(s)
  return 0 if ! s.include?("1")
  bins = {"0"=>"1", "1"=>"0"}
  first_1 = false
  ind = -1
  flips = 0
  while true
    s.each_char do |num|
      first_1 = true if num == "1"
      ind += 1
      next if first_1 == false
      s[ind] = bins[num]

    end
    flips += 1
    ind = -1
    first_1 = false
    return flips if ! s.include?("1")
  end
end
