list = [1,2,3]
dict = {
  'one':1,
  'two':2
}

# 호출
list[0] # 1호출
dict['one'] # 1호출 : 키로 호출

# 삭제
del(list[0])
del(dict['one'])

# 개수 확인
len(list)
len(dict)

# 값 확인
2 in list
'two' in dict.keys() # 값으로 확인할땐 : dict.values()

# 전부삭제
list.clear()
dict.clear()

# 업데이트
list1 + list2
dict1.update(dict2) # 키가 중복될시 dict1의 값을 dict2의 값으로 덮는다.