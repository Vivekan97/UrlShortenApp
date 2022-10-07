import unittest
from shortener import get_long_url, get_shortened_url

class MyTestCase(unittest.TestCase):
    
    url = "www.google.com"
    
    def test_get_shortened_url(self):
        assert(get_shortened_url(0), None)
        assert(get_shortened_url(""),None)
        assert(type(get_shortened_url(self.url)),str)
        assert(get_shortened_url(12345555),None)

    def test_get_long_url(self):
        assert(get_long_url(0), None)
        assert(get_long_url(""),None)
        assert(type(get_long_url(self.url)),str)
        assert(get_long_url(12345555),None)
        
    def test_short_long_logic(self):
        short = get_shortened_url(self.url)
        long = get_long_url(short)
        assert(short, long)
        assert(short, self.url)
        assert(self.url, long)    
        
        
if __name__=="__main__":
    unittest.main()