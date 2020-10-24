class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #逐行递归，当每一行都有一个皇后时即为满足条件返回一个结果。
        #初始化棋盘：由于字符串在python中为不可变量，故先用list[char]表示，再用''.join()拼接
        board = [['.' for _ in range(n)] for _ in range(n)]#初始化棋盘
        res=[]#存放最终结果

        def isValid(row,col):#判断（row,col）是否可行
            #逐行递归，判断(row,col)的每行/列/主对角/副对角是否只在(row,col)处有'Q'
            #判断row行：判断[row,0:col-1]是否有'Q'
            for c in range(col):#c:0->col-1
                if board[row][c] == 'Q':return False
            #判断col列：判断[0:row-1,col]是否有'Q'
            for r in range(row):#r:0->row-1
                if board[r][col] == 'Q':return False
            #判断(左上角)主对角线：判断[0:row-1,0:col-1]是否有'Q'
            mrow, mcol = row, col
            while mrow > 0 and mcol > 0:#mrow:0->row-1,mcol:0->row-1
                mrow-=1
                mcol-=1
                if board[mrow][mcol] == 'Q':return False
            #判断(右上角)副对角线：判断[0:row-1,col+1:n]
            vrow, vcol = row, col
            while vrow > 0 and vcol < n-1:#vrow:0->row-1,vcol:col+1->n
                vrow-=1
                vcol+=1
                if board[vrow][vcol] == 'Q':return False
            return True

        def DFS(res,row):#按行进行递归
            #递归基：若所有行都已放好Q，把结果写入,返回
            if row == n:
                temp=[]
                for line in board:
                    t = ''.join(line)
                    temp.append(t[:])
                res.append(temp[:])
                return
            #对该行的每一位置进行判断，找到适合放Q的位置，再递归深入到下一行，
            #到最后一行记录结果，并从下一行回溯到本行时恢复标记回溯到上行，
            for col in range(len(board[row])):
                if not isValid(row,col):continue#这个位置无效，判断下一个位置
                #若这个位置有效
                board[row][col] = 'Q'#找到位置添加标记
                DFS(res,row+1)#深入到下一行搜索可能位置
                board[row][col] = '.'#从下一行回溯到本行时恢复标记
        DFS(res,0)#DFS搜索
        return res