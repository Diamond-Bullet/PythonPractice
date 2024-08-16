import math
import random
import sys
import unittest


class TestBasics(unittest.TestCase):
    def test_identifier(self):
        """
        identifier can contain English letters, numbers and underscore, and can't start with numbers.
        it's case-sensitive.
        identifier starts with one underscore is protected class member, 需通过类提供的接口进行访问，不能用 from xxx import * 而导入。
        identifier starts with two underscores is private class member.
        以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。
        """

    def test_integer(self):
        integer1, integer2 = 10, 5

        # explicit data type conversion
        float1 = float(integer2)

        # funcs
        print(max(integer1, integer2))

        # `**` calculates `integer1` to the power `integer2`.
        print(integer1 * integer2, integer1 ** integer2, sep=', ')
        # `/` gives a float result in any case.
        # `//` returns an integer when both numerator and denominator are integers.
        print(integer1 / integer2, integer1 // integer2, sep=', ')

        integer1 &= integer2 | (integer2 << 3)
        integer1 ^= integer2  # XOR

    def test_float(self):
        f1, f2, f3, f4, f5 = 1.23, 2.5e2, 2.5e-4, math.pi, math.e

        c1 = 1 + 1j  # complex
        c2 = complex(1, 1)

        # data type conversion
        c3 = complex(f2, 4)

        # basic functions
        math.ceil(f1)
        math.floor(f1)
        math.sqrt(25.0)

        # random
        random.random()  # generate a real number in [0,1)
        random.choice(range(10))  # pick a number in given sequence

        # operators
        f4 += f1
        print(f2, f3)
        print(f1 == f2, f1 != f2, f1 >= f2, sep=', ')

    # string
    def test_string(self):
        #
        s1 = 'abcdef'
        s2 = "abcdef"

        # multiple lines string
        s3 = '''aaaa
        bbbb
        '''

        if 'a' in s1:
            print('a')

        if len(s1) > 4:
            print(s1[1:4])
        elif len(s1) > 5:
            print(s1[:6:2])
        else:
            print(s1[:-1:2])

    # list
    def test_list(self):
        l1 = [1, 2, 3, 5, 2, 3, 1]
        l2 = [1, 'a', 0.1]
        l3 = [[1], 1]
        l4 = [x ** 2 for x in range(10) if x % 2 == 1]  # list comprehension

        l1[1] = 4

        print(l1[:3])
        print(max(l1))

        # print elements in l1 via for-loop.
        for x in l1:
            if x == 7:
                break
            if x == 5:
                continue
            print(x, end=',')
        else:  # if for-loop finishes normally (not terminated by `break`), `else` will get executed.
            print("finish printing list")

    def test_tuple(self):
        # tuple is unmodifiable.
        t1 = (1,)
        t2 = (1, 2, 3)
        t3 = (1, 2, "a")
        t4 = t1 + t2

    def test_dict(self):
        d1 = {}
        d3 = {'a' + str(x): x for x in range(26)}

        d2 = {'a': 1, 'b': 'c', 'c': True}
        print(d2['a'])
        d2['a'] = 2
        d2['d'] = 3
        del d2['b']

        for key in d2:
            print(key)
        for key, value in d2.items():
            print(key, value)

        d2.clear()
        d2.keys()

    def test_set(self):
        s1 = set()
        s2 = {1, 3, 'a'}
        s3 = {x for x in 'abracadabra' if x not in 'abc'}

        s2.add(4)
        s2.update(s3)
        s2.discard(2)  # unlike remove(), no error occurs when element is not in set.

        if 3 in s2:
            print("3 in s2")

    def test_print(self):
        print("ss\nss")
        print("ss\tss")
        print("ss\rss")
        print('你好，世界')

    def test_exception(self):
        try:
            a = b = 10
            c, d = 0, 1
            a /= c
            b -= d
        except ZeroDivisionError as err:
            print(err)
        except BaseException as err1:  # all exceptions must subclass BaseException. hence, it catches all exceptions.
            # simply use `except` here is ok. it works the same as expression above.
            print(err1)
        else:  # run if no exception happens.
            print('no error')
        finally:  # always execute.
            print('anyway, I will get executed')

    def test_iterator(self):
        l = [1, 2, 3, 4, 5]
        il = iter(l)
        while True:
            try:
                next(il)
            except StopIteration as e:
                sys.exit()

    def test_my_print(self):
        my_print(10, "args", a=1, b=True)

    # open file
    # r: read, w: write, a: append, b: open in binary format,
    def test_open_file(self):
        file = open("/root/test", 'a')
        file1 = open("/root/test", 'wb')


# parameter with default value
def add(a, b=10):
    return a + b


# variable-length arguments
# *args refers to a tuple
# **kwargs refers to a dict
def my_print(self, a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)
