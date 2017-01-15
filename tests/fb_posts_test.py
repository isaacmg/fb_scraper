import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fb_posts_realtime import serialize

def fun(x):
    return x + 1


class MyTest(unittest.TestCase):
    def test(self):
        testList = ('115285708497149_1731636350195402', 'One-day special session, Northampton, MA YMCA.', 'Northampton Pool Rolling Session', 'event', 'https://www.facebook.com/events/319137738480268/', '2017-01-09 18:51:17', 1, 0, 0, 1, 0, 0, 0, 0, 0)
        s = serialize(testList)
        print(s)
        self.assertEqual(serialize(testList), 4)
if __name__ == '__main__':
    unittest.main()