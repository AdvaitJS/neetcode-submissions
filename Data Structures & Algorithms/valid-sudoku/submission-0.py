class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def box_indi(r , c):
            row , col = 0 , 0
            if r>=0 and r<=2: row = 0
            if r>=3 and r<=5: row = 1 
            if r>=6 and r<=8: row = 2
            if c>=0 and c<=2: col = 0
            if c>=3 and c<=5: col = 1 
            if c>=6 and c<=8: col = 2
            return row*3 + col 

            
        row = []
        col = []
        box = []
        for i in range(9):
            row.append(set())
            col.append(set())
            box.append(set())
        for r in range(9):
            for c in range(9):
                
                num = board[r][c]
                if num == ".":continue
                if num  in row[r] or num  in col[c]:
                    return False
                
                box_index = box_indi(r ,c )
                if num not in box[box_index]:
                    row[r].add(num)
                    col[c].add(num)
                    box[box_index].add(num)
                else:
                    return False
        return True