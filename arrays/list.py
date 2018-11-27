# simple number 1d array
numbers = [1, 200, 3, 4, 5]
# get first item of number array

# random indexing => O(1) get items if we know the index!
print(numbers[0])

for num in numbers:
    print('el numero es {}'.format(num))

# O(N) search running time if we dont know the index (linear time complexity)
maxium = numbers[0]
for num in numbers:
    if num > maxium:
        maxium = num

print('max es {}'.format(maxium))
print('done')
