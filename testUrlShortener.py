import shortenurl
import unittest
import json



class TestShortenUrl(unittest.TestCase):
    def test_print_hashes(self):
        with open('data.json', 'r') as file:
            data = json.load(file)
            self.assertEqual(list(shortenurl.run(['-h'])), list(data.keys()))
        
    def test_print_original_url(self):
        with open('data.json', 'r') as file:
            data = json.load(file)
            # print(data.values())
            # print(shortenurl.run(['-o']))
            self.assertEqual(list(shortenurl.run(['-o'])), list(data.values()))
        
    def test_print_all(self):
        with open('data.json', 'r') as file:
            data = json.load(file)
            self.assertEqual(shortenurl.run(['-a']), data)
    
    def test_get_original_url(self):
        with open('data.json', 'r') as file:
            data = json.load(file)
            self.assertEqual(shortenurl.run(['-g']), "Please provide a valid short url.")
        
            
    def test_valid_urls(self):
        tests = [
            ('http://www.cwi.nl:80/%7Eguido/Python.html', True), 
            ('/data/Python.html', False), 
            (532, False), 
            (u'dkakasdkjdjakdjadjfalskdjfalk', False), 
            ('https://stackoverflow.com', True)
        ]
        
        for (url, val) in tests:
            self.assertEqual(shortenurl.is_valid_url(url), val)
            


if __name__ == "__main__":
    unittest.main()
    
