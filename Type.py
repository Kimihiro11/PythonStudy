# -*- coding utf-8 -*-
class Hello(object):
    def hello(self,name='world'):
        print('Hello,%s.'%name)    

h = Hello()
h.hello()
print(type(Hello))
print(type(h))