# 튜플은 값의 변경과 삭제가 불가능

tuple1 = (1,2,3)
print(tuple1)
print(type(tuple1))

tuple2 = 1,2,3
print(tuple2)
print(type(tuple2))

list1 = [1,2,3]
tuple3 = tuple(list1)

print(tuple3)
print(type(tuple3))

print(tuple3[0])
print(tuple3[1])