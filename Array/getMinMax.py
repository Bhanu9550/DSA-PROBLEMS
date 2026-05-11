class Solution:
    def getMinMax(self, x):
        # code here
        if len(x)==1:
            return [x[0],x[0]]
        if x[0]>x[1]:
            max=x[0]
            min=x[1]
        else:
            max=x[1]
            min=x[0]
        if len(x)==2:
            return [min,max]
        for i in range(2,len(x)):
            if x[i]>max:
                max=x[i]
            elif x[i]<min:
                min=x[i]
        return [min,max]

run=Solution()
arr=[2,4,6,14,12,10,8]
print("Array of elements: ",arr)
print("Minimum and Maximum Elements in array: ",run.getMinMax(arr))