def rpsls(p1, p2)

    return "Draw!" if p1 == p2

    game_win = {'spock' => ['scissors', 'rock'], 
                'scissors'=> ['paper', 'lizard'], 
                'paper' => ['spock', 'rock'],
                'rock' => ['lizard','scissors'],
                'lizard' => ['paper', 'spock']}
      
    if game_win[p1].include?(p2) 
      return "Player 1 Won!" 
    end 
    
    "Player 2 Won!"
    
  end