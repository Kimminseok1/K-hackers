class study:
    name = "math"
    age = 1
    def __init__ (self,name,age):
        print('수업시작')
        self.name = name
        self. age = age
    def _del_ (self):
        print('수업끝')
    def info(self):
        print('이번 수업은',self.name,'입니다')
        print('시간은',self.age,'입니다')

class strong_study(study):
  weapon = 'pen'
  def __init__(self, name, age, weapon):
    print('strong_study 수업 호출!')
    super().__init__(name, age)
    self.weapon = weapon
  def info(self): 
    super().info()
    print(self.weapon, '로 공부합니다!')
