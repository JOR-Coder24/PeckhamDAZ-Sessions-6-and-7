import numpy as np

arr = np.array([3,1,4,1,5,9,3,2,6,5])


split_arr = np.array_split(arr, 2)#Splits array into 2
sorted_arr=np.sort(arr) #sorts array
filter_arr = arr % 2 == 0 #filters returns only even numbers
filtered_arr = arr[filter_arr]

print("The original array is: ",arr, ". The split array is ",split_arr, ". The sorted array is ", sorted_arr, ". The filtered away(which removes odd numbers) is ", filtered_arr)

