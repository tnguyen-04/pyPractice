def linear_search(array, number):
    length = len(array)
    for check in range(length):
        if array[check] == number:
            return check
    return False


arrayNumber = input('Enter an array of numbers ')
array = arrayNumber.split()
array = [int(number) for number in array]
find_number = int(input('what number do you want to find '))
position = linear_search(array, find_number)
if position is not False:
    print(f'The index of the number {find_number} is {position}')
else:
    print(f'The number {find_number} does not exist in the array')
    
# the complexity of the algorithm is O(n)  