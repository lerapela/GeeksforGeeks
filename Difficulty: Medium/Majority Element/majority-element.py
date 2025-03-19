#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        #Your code here
        
        candidate = None
        count =0
        
        for element in arr:
            
            if count == 0:
                candidate = element
            count += (1 if candidate == element  else -1)
            
        if arr.count(candidate) > len(arr)//2:
            
            return candidate
            
            
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends