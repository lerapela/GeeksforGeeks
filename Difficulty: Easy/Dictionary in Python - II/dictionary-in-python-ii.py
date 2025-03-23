#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

# Function to check if pair
# with given sum exists
def pair_sum(dict, arr, sum):
    # code here
    # Hint: You can use 'in' to find if any key is in dict
    for i in arr:
        if (sum-i) in dict:
            if (sum-i) != i:
                return True
    
    return False
        
    



#{ 
 # Driver Code Starts.
# Driver code
def main():
    
    # testcase input
    testcase = int(input())
    
    # looping through testcases
    while(testcase > 0):
        dict = {}
        arr = [int(i) for i in (input().split())]
        sum = int(input())
        
        for i in arr:
            dict[i] = 0
                
        for i in arr:
            dict[i] +=1
    
        if pair_sum(dict, arr, sum) is True:
            print ("true")
        else:
            print ("false")
        print("~")
        testcase -= 1


if __name__ == '__main__':
    main()
# } Driver Code Ends