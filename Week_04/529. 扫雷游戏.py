class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        '''
        [['E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'M', 'E', 'E'],
        ['B', 'B', 'E', 'E', 'E'],
        ['B', 'E', 'E', 'E', 'E']]
        '''
        dic=[[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]] #八个方向
        #for i,j in dic:dfs(x+i,y+j)
        def search_around(x,y): #看看周围几个雷
            count=0
            for i,j in dic:
                #if x+i<0 or x+i>n-1 or y+j<0 or y+j>m-1:
                #    continue
                if 0<=x+i<=n-1 and 0<=y+j<=m-1:
                    if board[x+i][y+j]=='M':
                        count+=1
            return count
        def dfs(x,y): #深度优先搜索
            if x<0 or x>n-1 or y<0 or y>m-1: #先判断边界
                return 
            if board[x][y]!='E': #再判断是不是E
                return 
            count=search_around(x,y) #算雷
            if count!=0: #有雷截断，不找了
                board[x][y]=str(count)
                return 
            else:
                board[x][y]='B'
                for i,j in dic:
                    dfs(x+i,y+j)
        n=len(board)
        m=len(board[0])
        #click=[a,b]
        if board[click[0]][click[1]]=='M': #有可能一开始就踩雷
            board[click[0]][click[1]]='X'
            return board
        else:
            dfs(click[0],click[1])
            return board