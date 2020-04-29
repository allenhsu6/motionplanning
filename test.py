# coding=utf-8

# 1. zip函数详解；参数列表；装饰器

# 2. 把jps做迁移

# 3. 不用做动图，没必要，画出来就行
import os
def test_zip():
    # 像一个拉链一样，将两个list链接起来
    x = [1,2,3]
    y = [4,5,6]
    z = [7,8,9]
    xyz = zip(x, y, z)
    print xyz

# 可变参数： 参数列表前加上 *
# python 允许在list 或者 tuple前加入 *, 实现将list或者tuple元素变为可变参数传入
# 这些参数在调用的时候，自动组装成一个tuple
def calc(*param):
    sum = 0
    for i in param:
        sum = sum + i
    return sum

# 关键字参数
# 允许传入任意个含有参数名的参数，函数内部自动装配成为dict
def person(name, age, **kwargs):
    print 'name: ', name, '\nage: ', age, '\nothers: ', kwargs


# python的高级特性
# 1. 所有对list的slice操作，在tuple都适用
def my_slice():
    a = list(range(10))
    print a
    print a[:3] + a[1:2]
    print a[-1:]
    print a[:10:2]
    print a[::-1]
# 2. iteration + list comprehension
def list_gen(*args):
    print [x*x for x in args if x % 2 == 1]
    print [d for d in os.listdir('/')]
# 3. generator
# a. 将列表生成式的[]改为()
# 通过for的迭代来使用generator
# b. 函数中包含yield关键字，这个函数就是一个generator
def yield_gen():
    g = (x * x for x in range(10))
    return g

def odd():
    print "step 1"
    yield 1
    print "step 2"
    yield 10
    print "step 3"
    yield 100

# higher-order function
# 一个函数接受另一个函数作为参数，这种函数称为高阶函数
# 1. map/reduce:例子略
# 2. filter
# 3. sorted



# 装饰器部分


if __name__ == "__main__":
    test_zip()
    num = [1,2,3]
    print calc(*num)
    print calc(2,3,4,5)
    print "==============="
    person('allen', 26, city='Beijing', job='engineer')
    extra = {'city': 'Beijing', 'job': 'painter'}
    person('miya', 27, **extra)
    print "=========="
    my_slice()
    print "=============="
    list_gen(*num)
    print yield_gen()
    g = yield_gen()
    for i in g:
        print i

    for i in odd():
        print i