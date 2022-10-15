import unittest
import os
import sys
try:
    from shortener import get_long_url, get_shortened_url
except ModuleNotFoundError as e:
    sys.path.append(os.getcwd())
    from shortener import get_long_url, get_shortened_url



class MyTestCase(unittest.TestCase):
    url = "http://www.google.com"
    print(os.getcwd())
    def test_get_shortened_url(self):
        self.assertIsNone(get_shortened_url(0))
        self.assertIs(get_shortened_url(""), "")
        self.assertIsInstance(get_shortened_url(self.url), str)
        self.assertIsInstance(get_shortened_url(12345555), str)

    def test_get_long_url(self):
        self.assertIsNone(get_long_url(0))
        self.assertIs(get_long_url(""), "")
        self.assertIsInstance(get_long_url(self.url), str)
        self.assertIsNone(get_long_url(12345555))
        
    def test_short_long_logic(self):
        short = get_shortened_url(self.url)
        long = get_long_url(short)
        self.assertNotEqual(short, long) 
        self.assertNotEqual(short, self.url) 
        self.assertEqual(self.url, long) 
        
        
if __name__ == "__main__":
    unittest.main()
