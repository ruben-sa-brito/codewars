#https://www.codewars.com/kata/586560a639c5ab3a260000f3
def rotate_2(str_, words):

    if len(words) == len(str_):
        return
    
    else:
        str_ = str_[1:] + str_[0]
        words.append(str_)
        rotate_2(str_, words)
    

def rotate(str_):
    rotate_list = list()
    
    rotate_2(str_, rotate_list)
    
    return rotate_list
