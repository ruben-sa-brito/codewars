'''
O codigo apresentado resolve o problema descrito a seguir:
Você mora na cidade de Cartesia, onde todas as estradas estão 
dispostas em uma grade perfeita. Você chegou dez minutos mais 
cedo para um compromisso, então decidiu aproveitar a 
oportunidade para dar uma curta caminhada. 
A cidade fornece aos seus cidadãos um aplicativo 
de geração de caminhada em seus telefones - 
toda vez que você pressiona o botão, ele envia uma 
série de strings de uma letra representando as direções para 
caminhar (por exemplo, ['n', 's', 'w', 'e']). Você sempre anda 
apenas um quarteirão para cada letra (direção) e sabe que leva 
um minuto para percorrer um quarteirão da cidade, então crie uma função 
que retornará true se a caminhada que o aplicativo lhe dá levar 
exatamente dez minutos (você não quero chegar cedo ou tarde!) 
e, é claro, o levará de volta ao seu ponto de partida. Devolva false caso contrário.

'''
def is_valid_walk(walk):
    
    if len(walk) == 10:

        if walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w'):
            return True
        else:
            return False

    else:
        return False   