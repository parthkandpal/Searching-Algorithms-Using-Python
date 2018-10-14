'''
In computer science, binary search, also known as half-interval search, logarithmic search, or binary chop,
is a search algorithm that finds the position of a target value within a sorted array.
Binary search compares the target value to the middle element of the array.

'''

def BinarySearch(Arr,n,x):
    start=0
    end=n-1
    while start<=end:
        mid = (start+end)//2

        if Arr[mid]==x:
            return mid
        elif x<Arr[mid]:
            end=mid-1
        else:
            start=mid+1

    return -1



Array=[21,33,35,39,45,78,86]
key=10
n=len(Array)
result=BinarySearch(Array,n,key)

if result==-1:
    print("Key not Found")
else:
    print("Key {} found at index {}".format(x,result))

