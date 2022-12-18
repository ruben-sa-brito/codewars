#https://www.codewars.com/kata/638244fb08da6c61361d2c40
def find_waldo(crowd):
    str1 = ''.join(crowd)
    list1 = list()
    
    x = 0
    y = 0
    for char in str1:
        list1.append(char)
    
    for str in crowd:
        y = 0
        for char in str:
            if list1.count(char) == 1:
                return [x , y]
            y +=1
        x += 1 
   
                
                
                