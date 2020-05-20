# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    i = 0
    j = 0
    current_index = 0 
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[current_index] = arrA[i]
            current_index += 1
            i += 1
        else:
            merged_arr[current_index] = arrB[j]
            j += 1
            current_index += 1

    while i < len(arrA):
        merged_arr[current_index] = arrA[i]
        i += 1
        current_index += 1

    while j < len(arrB):
        merged_arr[current_index] = arrB[j]
        j += 1
        current_index += 1
    print('Merged_arr :', merged_arr)
    return merged_arr
# arr_1 = [3,5,8,10]
# arr_2 = [6,12,15,19]
# print(merge(arr_1, arr_2))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code 
    if len(arr) > 1:
        mid = len(arr) //2 
        left = arr[:mid]
        print('Pre Sort Left: ', left)
        right = arr[mid:]
        print('Pre Sort Right: ',right)

        return merge(merge_sort(left), merge_sort(right))
        # print(left)
        # print(right)
        # merge_sort(left)
        # print('Post Merge Sort Left: ', left)

        # merge_sort(right)
        # print('Post Merge Sort Right: ', right)

        # print('Post Merge Left & Right: ', merge(left, right))
        

    return arr

my_arr = [4,1,2,23,3,5,6,2]
print(merge_sort(my_arr))

# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
