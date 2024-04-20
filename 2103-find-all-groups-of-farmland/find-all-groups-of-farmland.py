class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        R=len(land)
        C=len(land[0])

        used=[[False]*C for _ in range(R)]
        ans=[]

        for x in range(R):
            for y in range(C):
                if land[x][y]==1 and not used[x][y]:
                    sx,sy=x,y
                    ex,ey=sx,sy
                    while ey+1<C and land[ex][ey+1]==1:
                        ey+=1
                    while ex+1<R and land[ex+1][ey]==1:
                        ex+=1
                    ans.append((sx,sy,ex,ey))

                    for cx in range(sx,ex+1):
                        for cy in range(sy,ey+1):
                            used[cx][cy]=True
        return ans