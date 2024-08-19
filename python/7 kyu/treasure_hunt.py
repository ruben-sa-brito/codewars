# https://www.codewars.com/kata/66c0fec80a2a28b2a451d408
def find_treasure(grid, row, col):
    temp = grid[row-1][col-1]

    while True:
        if temp == grid[(temp//10)-1][(temp%10)-1]:
            return temp
        else: temp = grid[(temp//10)-1][(temp%10)-1]