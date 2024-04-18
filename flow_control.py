# -*- coding:utf-8 -*-
# 条件判断

# if 判断
name = 'xiao ming'
if name == 'xiao ming':
    print 'your name is', name

# if else 流程
if name == 'xiao ming':
    print 'if 分支通过',name
else:
    print 'else 分支通过' 

# if else if 流程 else if == esif
age = 14
if age >= 15:
    print '>=15 分支'
elif age <=18:
    print '>=18 分支'
else:  
    print 'else 分支'

# if 判断条件的简写比如写 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = None
if x:
    print 'Ture'
else: 
    print 'false'


