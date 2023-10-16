#https://www.codewars.com/kata/58de08d376f875dbb40000f1
def premier_league_standings(teams):
    
    return {team[0]+1:team[1] for team in enumerate([teams.pop(1)] + sorted(list(teams.values())))}