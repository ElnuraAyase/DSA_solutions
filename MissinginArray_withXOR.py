class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr) + 1 
        total_xor = 0
        xor_arr = 0
        
        for i in range (1, n+1):
            total_xor ^= i
            
        for num in arr:
            xor_arr ^= num
        
        return xor_arr ^ total_xor
        
s = Solution()
