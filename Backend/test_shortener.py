import unittest
from shortener import get_long_url, get_shortened_url


class MyTestCase(unittest.TestCase):
    url = "www.google.com"

    def test_get_shortened_url(self):
        self.assertIsNone(get_shortened_url(0))
        self.assertIs(get_shortened_url(""), "")
        assert type(get_shortened_url(self.url)) == str
        self.assertIsInstance(get_shortened_url(12345555), str)

    def test_get_long_url(self):
        self.assertIsNone(get_long_url(0))
        self.assertIs(get_long_url(""), "")
        assert type(get_long_url(self.url)), str
        assert get_long_url(12345555) is None
        
    def test_short_long_logic(self):
        short = get_shortened_url(self.url)
        long = get_long_url(short)
        assert short, long
        assert short, self.url
        assert self.url, long
        
        
if __name__ == "__main__":
    unittest.main()
