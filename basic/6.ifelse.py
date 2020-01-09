SCISSOR = '가위'
ROCK = '바위'
PAPER = '보'

WIN = '이겼다'
DRAW = '비겼다'
LOSE = '졌다..'

mine = '가위'
yours = '바위'


if mine == yours:
  result = DRAW
else:
  if mine == SCISSOR:
    if yours == ROCK:
      result = LOSE
    else:
      result = WIN
  elif mine == paper:
    if yours == SCISSOR:
      result = LOSE
    else:
      result = WIN
  else:
    print('이상함')

print(result)