def bubble_sort(list1):
    length_of_list = len(list1)
    for check1 in range(length_of_list):
        for check2 in range(0, length_of_list - check1 - 1):
            if list1[check2] > list1[check2 + 1]:
                list1[check2], list1[check2 + 1] = list1[check2 + 1], list1[check2]


list1 = [1, 4, 6, 7, 2, 8, 2, 5]
print(f'Before bubble sort : {list1}')
bubble_sort(list1)
print(f'After bubbler sort: {list1}')
print()


def selection_sort(array):
    length = len(array)
    for check1 in range(length - 1):
        temp = check1
        for check2 in range(check1 + 1, length):
            if array[check2] < array[temp]:
                temp = check2
        array[check1], array[temp] = array[temp], array[check1]


list2 = [1, 3, 5, 6, 5, 7, 8, 9]
print(f'Before selection sort : {list2}')
selection_sort(list2)
print(f'After selection sort : {list2}')

# Both the algorithms are O(n^2) time complexity and O(1) space complexity
