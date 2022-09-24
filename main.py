# BUBBLE SORT
#--------------------------------------------------------------------------------
def bubble_sort(arr):
    """
    Compares 2 indexes and when the front index is greater than the
    following index they will swap positions.

    Starting index: 0
    Index to compare to: 1
        Array: [2,1,3,4,7,5,9,8,6,0]
    2 and 1 will swap positions because 2 (index 0) is greater than 1 (index 1)
        New Array: [1,2,3,4,7,5,9,8,6,0]

    New starting index: 1
    New index to compare to: 2
        Array: [1,2,3,4,7,5,9,8,6,0]
    2 is smaller than 3 so it already is in its correct position and will not swap.
        New Array: [1,2,3,4,7,5,9,8,6,0]
    
    .
    .
    .
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            print("INDEX: ",j)
            print("COMP INDEX: ",j+1)
            print(arr)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)

# INSERTION SORT
#--------------------------------------------------------------------------------
def insertion_sort(arr):
    """
    The first index (0) is always considered sorted.
    This means, we first look at the second index (1).
    If index 1 is greater than index 0, it is considered sorted
    and the index will switch to index 2. 
    If index 2 is smaller than index 1 and also greater than index 0
    its value will be swapped (index 2 -> index 1).
    If index 4 is smaller than all its predecessors it will be moved to
    index 0, even though it completely skips over index 1,2 and 3.

        Array: [4,7,5,3,9,1,2]
    Already sorted index: 0
    New index: 1
    7 (index 1) is greater than 4 (index 0) so it is already sorted correctly.
        New Array: [4,7,5,3,9,1,2]
    
        Array: [4,7,5,3,9,1,2]
    Previous index: 1
    New Index: 2
    5 (index 2) is smaller than 7 (index 1) and greater than 4 (index 0), therefore
    it will swap values with index 1 (index 1: 5, index 2: 7)
        New Array: [4,5,7,3,9,1,2]

        Array: [4,5,7,3,9,1,2]
    Previous index: 2
    New index: 3
    3 (index 3) is smaller than its predecessor (index 2) and will therefore swap values
    with it (= index 2). However, it is also smaller than index 1 and index 0, therefore
    it is not sorted correctly and will be moved to index 0.
    """
    for a in range(1, len(arr)):
        b = a
        while b > 0 and arr[b] < arr[b-1]:
            arr[b-1],arr[b] = arr[b],arr[b-1]
            b -= 1
            print(arr)

# MERGE SORT
#--------------------------------------------------------------------------------
def merge_sort(arr: list):
    """
    The given array will always be split into 2 seperate parts until only one
    value of each side (right & left) remains.
    These two values will then be sorted adequatly.
    In case a value is the only value on one side the new seperated array the other
    side will be sorted first and then merged with the new array.

        Array: [4,9,6,3,1,8,0,7,2,5]
        Left: [4,9,6,3,1]       Right: [8,0,7,2,5]

    This is still too long so it will split into smaller parts

        Left: [4,9]             Right: [6,3,1]
        Left: [4]               Right: [9]

        This will now be sorted to be: [4, 9]
        Next up, the algorithm will look at [6, 3, 1]. Since this is too long, it will
        be split into:

        Left: [6]               Right: [3,1]
        Left: [3]               Right: [1]

        This will sorted into [1,3]. After this was sorted, the alogirthm will try to
        merge the [6] into the new sub-array [1,3]. The result will be: [1,3,6]
        After that, the original left side of the array is fully sorted into two 
        sub-arrays: [4,9] & [1,3,6]
        These will be merged together to represent the first half of the sorted array:
        [1,3,4,6,9]

        After this step is completed, the algorithm will repeat the same process with the
        original right side.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left  = arr[:mid]
        right = arr[mid:]
        print("LEFT: ",left,"RIGHT: ", right)
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0

        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        print(arr)

# QUICK SORT
#--------------------------------------------------------------------------------
def quick_sort(arr, left, right):
    """
    A Pivot-element will be picked (the last index in this case) and
    the other values in the array will be sorted by whether they are bigger
    or smaller than the given Pivot.
    Smaller values will be moved to the left side, greater ones to the right.
    After this, 2 other Pivots will be picked and the process will be repeated.
    This will yet again be repeated until there are no more elements left to sort.

        Array: [4,9,6,3,1,8,0,7,2,5]
                                  ^
                                Pivot
    It will now loop through the list and sort the values based on whether they
    are greater or smaller than 5.
        New Array: [4, 2, 0, 3, 1, 5, 6, 7, 9, 8]
                                ^
                            New Pivot
    The previous process will be repeated until everything is sorted based on
    whether its smaller or greater than 1.
        New Array: [0, 1, 4, 3, 2, 5, 6, 7, 9, 8]
                                ^
                            New Pivot
    .
    .
    .

    NOTE: In this scenario everything mentioned above is being handled in the partition() function!
    """
    if left < right:
        pi = partition(arr, left, right)

        quick_sort(arr, left, pi-1)
        quick_sort(arr, pi+1, right)

def partition(arr, left, right):
    """
    This splits the Array and sorts it accordingly.
    """
    i = left
    j = right - 1
    pivot = arr[right]
    print("PIVOT: ",pivot)

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
            print("INDEX (I): ",i,"     VALUE (ARR[I]): ",arr[i])

        while j > left and arr[j] >= pivot:
            j -= 1
            print("INDEX (J): ",j,"     VALUE (ARR[J]): ",arr[j])

        if i < j: 
            arr[i], arr[j] = arr[j], arr[i]
            print(arr)

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
        print(arr)

    return i













#--------------------------------------------------------------------------------
def sep():print("-"*80+"\n")
sample_list = [4,9,6,3,1,8,0,7,2,5]     #: sample array
print("ORIGINAL: ",sample_list)
sep()
# bubble_sort(sample_list)
# # sample_list = [4,9,6,3,1,8,0,7,2,5]
# sep()
# insertion_sort(sample_list)
# sample_list = [4,9,6,3,1,8,0,7,2,5]
# sep()
# merge_sort(sample_list)
# sample_list = [4,9,6,3,1,8,0,7,2,5]
# sep()
quick_sort(sample_list, 0, len(sample_list)-1)      #: NOTE: having the last index as the Pivot will decrease performance
sample_list = [4,9,6,3,1,8,0,7,2,5]