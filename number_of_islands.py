class Solution:
  # @param {character[][]} grid
  # @return {integer}
  def numIslands(self, grid):

    if not len(grid):
      return 0

    m, n = len(grid), len(grid[0])
    count = 0

    for i in xrange(m):
      for j in xrange(n):
        if grid[i][j] == "1":
          self.traverse(grid, m, n, i, j)
          count += 1
    return count

  def traverse(self, grid, m, n, i, j):

    if grid[i][j] == '0':
      return

    grid[i][j] = '0'

    if i != 0:
      self.traverse(grid, m, n, i - 1, j)

    if j != 0:
      self.traverse(grid, m, n, i, j - 1)

    if i + 1 < m:
      self.traverse(grid, m, n, i + 1, j)

    if j + 1 < n:
      self.traverse(grid, m, n, i, j + 1)

def main():

  grid1 = ["111","010","111"]
  print Solution().numIslands(grid1)



if __name__ == '__main__':
  main()