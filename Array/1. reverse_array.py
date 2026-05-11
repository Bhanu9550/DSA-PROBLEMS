class Solution:
    def reverseArray(self, x):
        end=len(x)-1
        for i in range(len(x)):
            if i<end:
                temp=x[i]
                x[i]=x[end]
                x[end]=temp
            end-=1
        return x

run=Solution()
arr=[2,3,5,7,9,11,13]
print("before reverse: ",arr)
print("after reverse: ",run.reverseArray(arr))