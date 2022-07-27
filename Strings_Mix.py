def mix(s1, s2):
    listnum = ['0','1','2','3','4','5','6','7','8','9']
    for num in s1:
        if num in listnum or not num.isalnum():
            s1 = s1.replace(num,'')
    for num in s2:
        if num in listnum or not num.isalnum():
            s2 = s2.replace(num,'')        
    
    lista1 = []
    lista2 = []

    for caractere1 in s1:
        if s1.count(caractere1) == s2.count(caractere1) and s1.count(caractere1) > 1:
            if caractere1 not in lista2:
                lista1.append('=:'+caractere1*s1.count(caractere1))
                lista2.append(caractere1)


        if not caractere1.isupper() and caractere1 not in lista2:
            if s1.count(caractere1) > s2.count(caractere1) and s1.count(caractere1)>1:
                lista1.append('1:'+caractere1*s1.count(caractere1))
                lista2.append(caractere1)

    for caractere2 in s2:
        if not caractere2.isupper() and caractere2 not in lista2:
            if s2.count(caractere2) > s1.count(caractere2) and s2.count(caractere2)>1:
                lista1.append('2:'+caractere2*s2.count(caractere2)) 
                lista2.append(caractere2)
         
    lista3 = []
    for x in lista1:
        lista3.append([len(x), x])
            
    if len(lista3) == 0:
        return ''
    x = 0
    lista4 = []
    cont = 0    
    
    while len(lista3) > 0:

        for a, b in lista3:
            cont += 1 
            
            if a > x:
                x = a
                c = b
                cont2 = cont - 1
            if len(lista3) == cont:
                cont = 0
                
                lista4.append(c)
                lista3.pop(cont2)
                cont2 = 0
                a = 0
                x = 0
                c = ''          
    z = len(lista4[0])
    
    lista5 = []
    lista6 = []
    
    while z >= 0:
        for y in lista4:
            if len(y) == z:
                lista5.append(y)
        z -= 1 
        lista5.sort()
        if lista5 != []:      
            lista6.append(lista5)
        lista5 = []

    string_mesclada = ''        
    for test1 in lista6:
        for testf in test1:
            string_mesclada += testf + '/'
    string_mesclada = string_mesclada[:-1]   
    return string_mesclada     

   
    

                    
                
s1, s2 ="Are they here", "yes, they are here"
print(mix(s1,s2))