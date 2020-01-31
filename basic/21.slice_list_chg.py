numbers = list(range(10))

del numbers[0]
# [1,2,3,4,5,6,7,8,9]

numbers[:5]
# [1,2,3,4,5]

del numbers[:5]
numbers
# [6,7,8,9]

numbers[1:3] = [77,88]
# [6,77,88,9]

numbers[1:3] = [77,88,99]
# [6,77,88,99,9]

numbers[1:4] = [8]
# [6,8,9]