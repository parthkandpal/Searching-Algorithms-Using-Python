#linearly search x in arr[].
# If x is present then return its  location,  otherwise
# return -1
def search(arr, x):
    for i in range(len(arr)):

        if arr[i] == x:
            return i

    return -1

arr=[1,2,3,4,5]

result=search(arr,5)

if result is -1:
    print("Element not Found")
else:
    print("Element found at index {}".format(result))


