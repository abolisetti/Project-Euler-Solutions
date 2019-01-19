def connect4(grid):
    ans = []
    for i in range(7):
        for j in range(3):
            
            ans += [grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]]
            ans += [grid[j][i]*grid[j+1][i]*grid[j+2][i]*grid[j+3][i]]

    for i in range(3):
        for j in range(3):
            ans += [grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]]
            
    for i in range(3,7):
        for j in range(3):
            ans += [grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3]]

    flag = True if max(ans) in (1,16) else False
    return flag

board = [[1,2,1,2,1,2,0],
         [0,2,0,2,1,2,0],
         [1,2,0,0,0,0,1],
         [1,0,0,1,0,0,0],
         [1,2,1,2,1,2,0],
         [2,2,2,1,1,2,0],
         [1,2,1,1,0,0,1]]
print(connect4(board))
