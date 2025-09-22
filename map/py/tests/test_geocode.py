import os
import unittest
from davidkhala.baidu.map import API


class MyTestCase(unittest.TestCase):

    def setUp(self):
        ak = os.environ.get("AK")
        self.api = API(ak)
    def test_location(self):
        r = self.api.get_location("重慶市雲陽雙江中學校")
        print(r)

    def test_location_en(self):

        r = self.api.geocoding("Fuqing No. 1 High School")
        self.assertEqual(r['level'],'购物') # mismatch
        r = self.api.geocoding("福清一中")
        self.assertEqual(r['level'],'教育') # match


if __name__ == '__main__':
    unittest.main()
