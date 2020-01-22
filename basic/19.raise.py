# def rsp(mine, yours):
#   alllowed = ['가위','바위','보']
#   if mine not in alllowed:
#     raise ValueError
#   if yours not in alllowed:
#     raise ValueError

# try:
#   rsp('가위','바')
# except ValueError:
#   print('잘못된 값입니다.')

school = {'1반': [172,18,198,177,165,199], '2반':[165,177,167,180,191]}

try:
  for class_number, students in school.items():
    for student in students:
      if student>190:
        print(class_number,'반에 190을 넘는 학생이 있습니다.')
        raise StopIteration
except StopIteration:
  print('정상종료')