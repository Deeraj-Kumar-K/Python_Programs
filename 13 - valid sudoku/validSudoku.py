# https://leetcode.com/problems/valid-sudoku/

# Check Sudoku board is valid or not
# if valid return True otherwise False

def check(board):
    hashTable={}
    # For checking each row
    for row in board:
        for i in range(9):
            if row[i] in hashTable and row[i]!='.':
                print("Row",row[i])
                return False
            else:
                hashTable[row[i]] = True
        hashTable={}
  
    # For checking each column 
    for i in range(9):
        for j in range(9):
            if board[j][i] in hashTable and board[j][i]!='.':
                print("COL",board[j][i])
                return False
            else:
                hashTable[board[j][i]] = True
        hashTable={}
        
    # For checking each 3x3 sub-boxes 
    c=0
    r=0
    for k in range(9):
        if k==3 or k==6:
            c=0
            r+=3
        for i in range(3):
            for j in range(3):
                if board[i+r][j+c] in hashTable and board[i+r][j+c]!='.':
                    return False
                else:
                    hashTable[board[i+r][j+c]] = True
        hashTable={}
        c+=3
    
    return True
            
            
board = [
["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

#3x3 sub-box in the top right corner have two 1's
# therefore Output: False (not valid sudoku)
board2 = [
[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]]

print("For 1st input:",check(board))
print("For 2nd input:",check(board2))
