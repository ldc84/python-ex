my_list = [1,2,3,4,5]
my_list(0) # 1

str = 'Hello World'
str[0]  # 'H'

3 in my_list  #True

"H" in str # True

my_list.index(5)  # 4

str.index('r')  # 9

characters = list('abcdef')
characters  # ['a','b','c','d','e','f']

words = 'Hello World'
words_list = words.split()
words_list  # ['Hello', 'World']

time_str = '10:35:27'
time_list = time_str.split(':')
time_list # ['10', '35', '27']

':'.join(time_list) # '10:35:27'

' '.join(words_list)  # 'Hello World'