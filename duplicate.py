''' 
esse codigo funciona recebendo uma string como parametro e verificando as
letras que se repetem nessa string retornando a quantidade de letras que se repetem
sem fazer distinção entre letras maisculas e minusculas
(independente de quantas vezes elas se repetirem), exemplos:
"aabbccdef" - essa string deve retornar 3
"aabbcc223xe" - essa string deve tretornar 4
"acdafxf55ABB" - essa string deve tretornar 4

'''



def duplicate_count(text):

    list1 = list(text.lower()) 

    morethanonce = 0 

    for first_char in text:
        cont = 0 
        list1.pop(0)
        count3 = 1
        for second_char in list1:
            if first_char.lower() == second_char:
                cont += 1
            if len(list1) == count3:
                if not cont > 1:
                    if cont != 0:
                        morethanonce += 1
            count3 += 1 
    return morethanonce
    
print(duplicate_count('aabbccdef'))