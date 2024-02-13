//https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9
function findShort(s){

    let words = s.split(" ")
    let words_len = words.map(x => 
        x.length)

    return Math.min.apply(Math, words_len)
      
}