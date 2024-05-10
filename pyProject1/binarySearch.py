# the algorithm find the position of a number in an array
def binarySearch(array, number):
    length = len(array)
    left = 0
    right = length - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == number:
            return mid
        elif array[mid] > number:
            right = mid - 1
        else:
            left = mid + 1
    return False


# handle the string entered by user into integer

arrayNumber = input('Enter an array of numbers ')
array = [int(number) for number in arrayNumber.split()]
find_number = int(input('what number do you want to find '))
position = binarySearch(array, find_number)
if position is not False:
    print(f'The index of the number that you are finding is : {position}')
else:
    print(f'This number {find_number} does not exist in the array')

# the complexity of the algorithm is O(log(n)





          
