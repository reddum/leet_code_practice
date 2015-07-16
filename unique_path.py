class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
      
      matrix=[[0 for y in range(n + 1)] for x in range(m + 1)] 
      matrix[1][1]= 1
      y=1
      while y<=n:
          x=1
          while x<=m:
              if x== 1 and y == 1:
                  pass
              else:
                matrix[x][y]=matrix[x-1][y]+matrix[x][y-1]
              x+=1
          y+=1
      return matrix[m][n]

