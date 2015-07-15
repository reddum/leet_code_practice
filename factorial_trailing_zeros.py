import sys

class Solution:
  # @param {integer} n
  # @return {integer}
  def trailingZeroes(self, n):
    f = 5
    count = 0
    while n >= f:
      count += n / f
      f *= 5
    return count

if __name__ == "__main__":

	if len(sys.argv) == 2:
		print Solution().trailingZeroes(int(sys.argv[1]))
