# -*- coding:utf-8-*-
# 循环
array = ['a','b','c','d']
for item in array:
    print item

# range() 函数 可以生成一个整数序列
list = range(7)
print list

# while 只要条件满足，就不断循环，条件不满足时退出循环
num = 10
n = 0
while num >0:
    n = n+num
    num = num-1
print n

value = raw_input('value:')
print value
print isinstance(value, int)
