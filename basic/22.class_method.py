class Human():
  '''인간'''
  def __init__(self, name, weight):
    '''초기화함수'''
    self.name = name
    self.weight = weight

  def __str__(self):
    '''문자열화 함수'''
    return '{} (몸무게 {}kg)'.format(self.name, self.weight)

  # ___init___ 함수가 대신 할 수 있다
  # def create(name, weight):
  #   person = Human()
  #   person.name = name
  #   person.weight = weight
  #   return person
    
  def eat(self):
    self.weight += 0.1
    print('{}가 먹어서 {}kg이 되었습니다.'.format(self.name, self.weight))

  def walk(self):
    self.weight -= 0.1
    print('{}가 걸어서 {}kg이 되었습니다.'.format(self.name, self.weight))

  def speak(self, message):
    print(message)

person = Human('사람', 60.5)
print(person)