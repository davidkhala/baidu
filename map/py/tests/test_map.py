import os
import unittest
from davidkhala.baidu.map import API


class GeoCodeTestCase(unittest.TestCase):

    def setUp(self):
        ak = os.environ.get("AK")
        self.api = API(ak)

    def test_location(self):
        r = self.api.geocoding("重慶市雲陽雙江中學校")
        print(r)

    def test_location_en(self):
        r = self.api.geocoding("Fuqing No. 1 High School")
        self.assertEqual('购物', r['level'])  # mismatch
        r = self.api.geocoding("福清一中")
        self.assertEqual('教育', r['level'])  # match


class PlaceTestCase(unittest.TestCase):
    def setUp(self):
        ak = os.environ.get("AK")
        self.api = API(ak)

    def test_region(self):
        r, total = self.api.place('柳州高級中學')
        self.assertEqual(72,total)

    def test_suggest(self):
        r = self.api.suggest('柳州高級中學')
        self.assertEqual(10, len(r))


if __name__ == '__main__':
    unittest.main()
