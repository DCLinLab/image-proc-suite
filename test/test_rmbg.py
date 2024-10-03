import unittest
from scripts.rm_bg import main
from pathlib import Path


class MyTestCase(unittest.TestCase):
    def test_something(self):
        fd = Path(r'C:\Users\Zuohan Zhao\Desktop\HY041')
        ofd = Path(r'C:\Users\Zuohan Zhao\Desktop\HY041_after')
        for i in fd.glob('*.tif'):
            main(i, ofd / i.name)


if __name__ == '__main__':
    unittest.main()
