class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        
        candidate1,  candidate2 = None, None
        count1, count2 =0, 0
        
        for element in arr:
            
            if  candidate1 == element:
                count1 +=1
            elif candidate2 == element:
                count2 +=1
                
            elif count1 == 0:
                candidate1, count1=element,1
            elif count2 == 0:
                candidate2, count2=element,1
                
            else:
                count1 -=1
                count2 -=1
            
            
            
        results = [] 
            
            
        if arr.count(candidate1) > len(arr)//3:
             results.append(candidate1)
            
        if arr.count(candidate2) > len(arr)//3:
             results.append(candidate2)
            
            
            
        results.sort()   
            
        return results


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends