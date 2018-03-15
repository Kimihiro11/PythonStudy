# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if L==[]:
        return (None,None)
    Min=Max=L[0]
    for i in L:
        if i<=Min:
            Min=i
        elif i>=Max:
            Max=i
    print(Min,Max)
    return (Min,Max)
        


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
        