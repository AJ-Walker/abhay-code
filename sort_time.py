from time import *

def insertion_sort():
    for j in range(1,n):
        key=a[j]
        i=j-1
        while i>=0 and a[i]>key:
            a[i+1]=a[i]
            i=i-1
            a[i+1]=key            
            #print('\nstep ',count,':',a)
            
    print('\nSorted List:', a)              

def partition(lo, hi):
    pivot = a[hi]
    i=lo    #place for swapping
    for j in range (lo, hi):
        if a[j] <= pivot:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
            i=i+1
        #print('pivot: ', pivot, 'List: ',a)
    temp=a[i]
    a[i]=a[hi]
    a[hi]=temp
    return i
def quick_sort(lo,hi):
    if lo < hi:
        p = partition(lo,hi)
        quick_sort(lo, p-1)
        quick_sort(p+1, hi)
        
a=[]
n=int(input('Enter the number of elements: '))
for i in range(0,n):
    num=input('Enter the value: ')
    a.append(num)
#start_time = time()
start_time = clock()
#insertion_sort()
quick_sort(0, n-1)
#end_time = time()
end_time = clock()
exe_time = end_time - start_time
print('\nExecution time is ',exe_time, 'Seconds')
print(a)
