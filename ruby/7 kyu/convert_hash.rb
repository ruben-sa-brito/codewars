#https://www.codewars.com/kata/59557b2a6e595316ab000046
def convert_hash_to_array(hash)
    array = []
    hash.each do |element|
        array.push([element[0].to_s, element[1]])
    end   
    array
end