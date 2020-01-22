a, b = 1, 2
print(a, b)

c = (3,4)
print(c)

d, e = c
print(d, e)

f = d, e
print(f)

x = 5
y = 10
print(x, y)

x, y = y, x
print(x, y)

def tuple_func():
  return 1, 2
q, w = tuple_func()
print(q, w)