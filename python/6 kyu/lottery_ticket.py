#https://www.codewars.com/kata/57f625992f4d53c24200070e
def bingo(tickets,win):
    total = 0
    for ticket in tickets:
        if len(list(filter(lambda play: ord(play[0]) == ticket[1], ticket[0]))) >= 1: total+=1
    return 'Loser!' if total < win else 'Winner!'