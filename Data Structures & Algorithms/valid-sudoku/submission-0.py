class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i, line in enumerate(board):
            horizontal_check = [number for number in line if number != '.']
            if len(horizontal_check) != len(set(horizontal_check)):return False
            vertical_check = [line[i] for line in board if line[i]!= '.']
            if len(vertical_check) != len(set(vertical_check)):return False
        
            box = []
            for j in range(3):
                box.extend(board[j+ (i//3)*3][i*3%9:i*3%9+3])
            box = [number for number in box if number != '.']
            if len(box) != len(set(box)):return False            
        

        return True