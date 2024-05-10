#The case if the pivot = a[0]
def quickSort1(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less_than_pivot = [x for x in array[1:] if x <= pivot]
        greater_than_pivot = [x for x in array[1:] if x > pivot]
        return quickSort1(less_than_pivot) + [pivot] + quickSort1(greater_than_pivot)

lis1 = [3, 3, 5, 67, 2, 5, 6, 5, 66, 8, 9, 45, 33, 67, 88, 79]
print(f'before sorting {lis1}')
lis1 = quickSort1(lis1)
print(f'after sorting {lis1}')

print('\n'*2)
#the case if the pivot is in middle 
def quickSort2(array):
    if len(array) <= 1:
        return array
    else:
        mid_index = len(array)//2
        pivot = array[mid_index]
        less_than_pivot = [x for i, x in enumerate(array) if i!= mid_index and x <= pivot]
        greater_than_pivot = [x for i, x in enumerate(array) if i!= mid_index and x > pivot]
        return quickSort1(less_than_pivot) + [pivot] + quickSort1(greater_than_pivot)

lis2 = [100,2,3,33,44,52,5,6,7,9,10]
print(f'before sorting {lis2}')
lis2 = quickSort2(lis2)
print(f'after sorting {lis2}')