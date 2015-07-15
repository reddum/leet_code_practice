class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
    
        nums3 = []
        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        while i < m:
            nums3.append(nums1[i])
            i += 1
        while j < n:
            nums3.append(nums2[j])
            j += 1
        nums1[:] = nums3
        
    
        