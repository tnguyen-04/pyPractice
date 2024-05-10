def insertionSort(array):
    length = len(array)
    for check1 in range(1, length):
        pre = array[check1]
        behind = check1 - 1 
        while behind >= 0 and array[behind] > pre:
           array[behind +1] =array[behind]
           behind = behind -1
        array[behind +1] = pre
        
list1 = [8,3,5,7,4,9,3,6]
insertionSort(list1)
print(list1)
    
    
    

          