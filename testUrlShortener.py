import shortenurl
import unittest
import json



class TestShortenUrl(unittest.TestCase):
    def test_print_hashes(self):
        with open('data.json', 'r') as file:
            data = json.load(file)
            self.assertEqual(list(shortenurl.run(['-h'])), list(data.keys()))
        
    def test_original_url(self):
        with open('data.json', 'r') as file:
            data = json.load(file)
            # print(data.values())
            # print(shortenurl.run(['-o']))
            self.assertEqual(list(shortenurl.run(['-o'])), list(data.values()))
            


if __name__ == "__main__":
    unittest.main()
    
