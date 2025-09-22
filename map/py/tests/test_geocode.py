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


if __name__ == '__main__':
    unittest.main()
