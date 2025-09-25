class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr) + 1 # total nums from 1 to n inside given arr
        
        total_sum = n * (n+1) // 2 # total sum of nums in arr
        
        array_sum = sum(arr) # sum of numbers in given arr
        
        return total_sum - array_sum
        
solu = Solution()
