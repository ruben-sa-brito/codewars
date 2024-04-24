#https://www.codewars.com/kata/586ec0b8d098206cce001141
def inverse_slice(items, a, b)

    begin
      items[0...a] + items[b..-1]
    rescue 
      return items[0...a]
    end
    
  end