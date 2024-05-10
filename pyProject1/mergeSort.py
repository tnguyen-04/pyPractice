def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        half_left = arr[:mid]
        half_right = arr[mid:]
    
        mergeSort(half_left)
        mergeSort(half_right)
        
        i = j = k = 0
        while i < len(half_left) and j < len(half_right):
            if half_left[i] < half_right[j]:
                arr[k] = half_left [i]
                i+=1
            else: 
                arr[k] = half_right[j]
                j+=1
            k+=1
        while i < len(half_left):
            arr[k] = half_left[i]
            i+=1
            k+=1
        while j < len(half_right):
            arr[k] = half_right[j]
            j+=1
            k+=1
    return arr    
lis1 = [2, 4, 2, 9, 5, 8, 7, 3, 0]
print(f'before{lis1}')

lis1 = mergeSort(lis1)
print()
print(f'After{lis1} ')


# another shorter way
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = mergeSort(arr[:mid])
    right_half = mergeSort(arr[mid:])
    
    sorted_arr = []
    left_index = right_index = 0
    
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            sorted_arr.append(left_half[left_index])
            left_index += 1
        else:
            sorted_arr.append(right_half[right_index])
            right_index += 1
            
    sorted_arr.extend(left_half[left_index:])
    sorted_arr.extend(right_half[right_index:])
    
    return sorted_arr

# Sử dụng hàm mergeSort
arr = [12, 11, 13, 5, 6, 7]
print("Dãy ban đầu:", arr)
sorted_arr = mergeSort(arr)
print("Dãy đã sắp xếp:", sorted_arr)
