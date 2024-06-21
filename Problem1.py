#Taking all required inputs.
N = int(input())
k = int(input())
array = []

#Loop to inserting array elements
for i in range(N):
    element = int(input())
    array.append(element)
print(array)

#Creating variables for the logic
maxSum = 0
pos = 0

#fetching sub array of length k 

while pos <= len(array)-2:
    sb_array = array[pos:pos+2]
    pos += 1

    #finding maximum sum sub array2
    if maxSum < sum(sb_array):
        maxSum = sum(sb_array)
    else: continue

#result
print(maxSum)
