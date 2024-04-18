# -*- coding: utf-8 -*-
#list and tuple

#list 

a = ['a','b','c']
print a

# sb gy


# list 长度
print len(a)

# list 索引  从0开始   也可以倒序从-1 开始
print a[0],a[-1]

# 向list末尾添加元素  使用append()
a.append(1)
print a

# 删除list 中的元素pop(index)  pop() 默认删除最后的元素  index 为索引值
a.pop()
print a

# 向指定位置添加元素 insert(index, item)
a.insert(0, 'hello world')
print a

# list 既可以是一维  也可以是多维

# tuple 元组
# 有序列表元组tuple和list非常类似，但是tuple一旦初始化就不能修改
a=('a','b','c')
print a
print a[0]

# 为区分与数学中的小括号 定义一个元素时 需要加,
b=('a',)
c=('abc')
print b,c
