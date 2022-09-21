def encrypt_this(text):
    words = []
    word = str()
    new_s = str()
    if text == '':
        return ''
    
    for l in text:
        if l == ' ':
            words.append(word)
            word = ''
            l=''
        word += l
        
    else:
        words.append(word)     
    
    for word in words:
        
        if len(word) == 1:
            new_s += str(ord(word[0])) + ' '
            
        elif (len(word) > 2) :
            new_s += str(ord(word[0])) + word[-1] + word[2:-1] + word[1]+ ' '
            
        else:
            new_s += str(ord(word[0])) + word[1:] + ' '   
    
    return new_s[:-1]

        