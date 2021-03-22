# merge() merges two subarrays of arr[1eft..right]
# First subarray is arr[left..middle]
# Second subarray is arr[middle+1..right]
def merge(arr, left, middle, right):
    n1 = middle - left + 1
    n2 = right- middle
 
    # create temp arrays
    L = []
    R = []
    for i in range(0 , n1):
        L.append(0)
 
    for j in range(0 , n2):
        R.append(0)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0 , n1):
        L[i] = arr[left + i]
 
    for j in range(0 , n2):
        R[j] = arr[middle + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Starting index of first subarray
    j = 0     # Starting index of second subarray
    k = left     # Starting index of merged subarray
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# left is for left index and right is right index of the
# sub-array of arr to be sorted
def mergeSort(arr,left,right):
    if left < right:
        middle = (left+(right-1))//2
 
        # Sort first and second halves
        mergeSort(arr, left, middle)
        mergeSort(arr, middle+1, right)
        merge(arr, left, middle, right)


arr = []

cont = 'Y'
while cont == 'y' or cont == 'Y':
    data = int(input('Enter the element: '))
    arr.append(data)
    cont = input('Continue? (Y/N): ')


n = len(arr)
print ("Given array is")
for i in range(n):
    print (arr[i])
 
mergeSort(arr,0,n-1)
print ("\n\nSorted array is")
for i in range(n):
    print (arr[i])