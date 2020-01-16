list = [1,2,3,4,5]
list[2] = 33

print(list)

list.append(6)

print(list)

dict = {
  'one':1,
  'two':2
}

dict['one'] = 11
print(dict)

dict['three'] = 3
print(dict)

# 지우기
del (list[0])
print(list)

del dict['one']
print(dict)

list.pop(0) # pop() : 지우고 해당 인덱스를 반환
print(list)

dict.pop('two')
print(dict)