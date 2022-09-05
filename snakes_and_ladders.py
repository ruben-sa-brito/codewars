class SnakesLadders():

    def __init__(self):
        self.snake = {16:6, 46:25, 49:11, 62:19, 64:60, 74:53, 89:68, 92:88, 95:75, 99:80}
        self.ladder = {2:38, 7:14, 8:31, 15:26, 21:42, 28:84, 36:44, 51:67, 71:91, 78:98, 87:94}
        self.player1_sqr = 0
        self.player2_sqr = 0
        self.player = 1
        self.gameover = False
        self.strreturn = ''

    def play(self, die1, die2):
        if self.gameover == True:
            return 'Game over!'

        if self.player == 1:

            self.player1_sqr += die1 + die2

            if self.player1_sqr == 100:
                self.gameover = True
                return f'Player {self.player} Wins!'

            if self.player1_sqr > 100:
                self.player1_sqr = 100-(self.player1_sqr-100)

            if self.player1_sqr in self.snake:
                self.player1_sqr = self.snake[self.player1_sqr]
            elif self.player1_sqr in self.ladder:
                self.player1_sqr = self.ladder[self.player1_sqr]

            self.strreturn = f'Player {self.player} is on square {self.player1_sqr}'    

        else:

            self.player2_sqr += die1 + die2

            if self.player2_sqr == 100:
                self.gameover = True
                return f'Player {self.player} Wins!'


            if self.player2_sqr > 100:
                self.player2_sqr = 100-(self.player2_sqr-100)

            if self.player2_sqr in self.snake:
                self.player2_sqr = self.snake[self.player2_sqr]
            elif self.player2_sqr in self.ladder:
                self.player2_sqr = self.ladder[self.player2_sqr]

            self.strreturn = f'Player {self.player} is on square {self.player2_sqr}'     



        if self.player == 1 and die1 != die2:
            self.player = 2
        elif self.player == 2 and die1 !=die2:
            self.player = 1 

        return self.strreturn              