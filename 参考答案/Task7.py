import doctest
import unittest


# Problem1
def calu(a, b, op):
    """
    以下为第四题文档测试内容

    >>> calu(1, 2, "+")
    3
    >>> calu(1, 2, "-")
    -1
    >>> calu(1, 2, "*")
    2
    >>> calu(1, 2, "/")
    0.5
    >>> calu(1, 0, "/")
    Caught an Exception:
    Exception Type: ZeroDivisionError
    Exception Info: division by zero
    """

    ans = 0
    try:
        if op == "+":
            ans = a+b
        elif op == "-":
            ans = a-b
        elif op == "*":
            ans = a*b
        elif op == "/":
            ans = a/b
        else:
            print("Wrong parameter 'op'")
        return ans
    except Exception as e:
        print(f"""\
Caught an Exception:
Exception Type: {type(e).__name__}
Exception Info: {str(e)}\
""")


# Problem2
def devide(a, b):
    if b == 0:
        raise ZeroDivisionError("把0当除数你是不是傻啊？")
    return a/b


# Problem3
class TestDevide(unittest.TestCase):
    def test_common(self):
        self.assertEqual(devide(5, 1), 5)
        self.assertEqual(devide(6, 4), 1.5)

    def test_exception(self):
        with self.assertRaises(ZeroDivisionError):
            devide(5, 0)


# devide(1, 0)
doctest.testmod()
unittest.main()
