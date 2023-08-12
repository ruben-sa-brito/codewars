//https://www.codewars.com/kata/570597e258b58f6edc00230d/train/javascript
function array(string) {

    let count = string.split(',')

    if (count.length < 3) {

        return null

    } else {
        count  = count.slice(1,-1)
        count = count.join(" ")
        return count

    }

}
 