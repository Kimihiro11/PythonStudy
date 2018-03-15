# -*- coding utf-8 -*-
class Student(object):

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer')
        if  value <0 or value >100:
           raise ValueError('score must between 0~100!')
        self._score = value

#s = Student()
#s.score = 60
#print(s.score)

class Screen(object):

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height = value

    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self,value):
        self._weight = value

    @property
    def resolution(self):
        return self._height*self._weight

# 测试:
s = Screen()
s.weight = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')    
  