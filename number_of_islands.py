class Solution:
  # @param {character[][]} grid
  # @return {integer}
  def numIslands(self, grid):

    if not len(grid):
      return 0

    m, n = len(grid), len(grid[0])
    verified = [[False] * n for x in range(m)]
    count = 0

    for i in range(m):
      for j in range(n):
        if grid[i][j] == "1" and not verified[i][j]:
          self.traverse(grid, verified, m, n, i, j)
          count += 1
    return count

  def traverse(self, grid, verified, m, n, i, j):

    if grid[i][j] == '0':
      verified[i][j] = True
      return

    if verified[i][j]:
      return

    verified[i][j] = True

    if i != 0:
      self.traverse(grid, verified, m, n, i - 1, j)

    if j != 0:
      self.traverse(grid, verified, m, n, i, j - 1)

    if i + 1 < m:
      self.traverse(grid, verified, m, n, i + 1, j)

    if j + 1 < n:
      self.traverse(grid, verified, m, n, i, j + 1)

def main():

  grid1 = ["111","010","111"]
  print Solution().numIslands(grid1)



if __name__ == '__main__':
  main()