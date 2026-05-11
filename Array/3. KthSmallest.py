class Solution:
    def kthSmallest(self, x, k):
        # Code here
        # for i in range(k):
        #     for j in range(len(x)-i):
        #         if j==len(x)-1:
        #             continue
        #         if x[j]<x[j+1]:
        #             temp=x[j+1]
        #             x[j+1]=x[j]
        #             x[j]=temp
        # return x[-k]

        # Even also it is not optimized code

        for i in range(1,k+1):
            if x[0]<x[1]:
                min=x[0]
            else:
                min=x[1]
            for j in range(len(x)):
                if min>x[j]:
                    min=x[j]
            if i==k:
                return min
            x.remove(min)
        
run=Solution()
arr=[2,8,10,56,14,7,6,1]
k=2
print("array: ",arr, "Kth value: ",k)
print("Kth Smallest Value: ",run.kthSmallest(arr,k))