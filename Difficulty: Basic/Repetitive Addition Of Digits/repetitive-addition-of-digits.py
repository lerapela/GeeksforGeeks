class Solution:
    def singleDigit(self, n):
    	#code here 
    	
        while n >= 10:
            n = sum(int(digit) for digit in str(n))
        return n
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.singleDigit(N)
        print(ans)
        print("~")

# } Driver Code Ends