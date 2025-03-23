class Solution:
    def canPair(self, arr, k):
        #code here.
        if len(arr)%2 !=0:
            return False
        
        remainder_count = {}
        
      
        for num in arr:
            remainder = num % k
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
        
       
        for remainder in remainder_count:
            if remainder == 0:  
               
                if remainder_count[remainder] % 2 != 0:
                    return False
            elif remainder * 2 == k:
               
                if remainder_count[remainder] % 2 != 0:
                    return False
            else:
                
                if remainder_count[remainder] != remainder_count.get(k - remainder, 0):
                    return False
        
        return True
            


#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())

        solution = Solution()
        ans = solution.canPair(arr, k)
        print("true" if ans else "false")


if __name__ == "__main__":
    main()

# } Driver Code Ends