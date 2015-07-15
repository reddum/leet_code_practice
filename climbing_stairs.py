class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        p = 1
        q = 1

        for i in range(1, n):
        	temp = q 
        	q += p
        	p = temp

        return q
