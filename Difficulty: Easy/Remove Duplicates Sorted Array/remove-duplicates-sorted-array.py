#User function template for Python
import numpy as np
class Solution:
    def removeDuplicates(self, arr):
        #Code Here
        arr_np = np.array(arr)
        
         
        unique_arr = np.unique(arr_np)
        
       
        arr[:len(unique_arr)] = unique_arr
        
       
        return len(unique_arr)
#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    line = 1

    solution = Solution()

    for _ in range(t):
        if line < len(data):
            arr = list(map(int, data[line].split()))
            line += 1
            ans = solution.removeDuplicates(arr)
            for i in range(ans):
                print(arr[i], end=" ")
            print()
        print("~")

# } Driver Code Ends