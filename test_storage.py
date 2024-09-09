import unittest
from unittest.mock import mock_open, patch
import json

class TestStorage(unittest.TestCase):

    # Test for get_data function
    @patch("builtins.open", new_callable=mock_open, read_data='{"abc123": "https://example.com"}')
    def test_get_data(self, mock_file):
        from storage import get_data
        data = get_data()
        self.assertEqual(data, {"abc123": "https://example.com"})
        mock_file.assert_called_once_with('data.json', 'r')

    # Test for save_data function
    @patch("builtins.open", new_callable=mock_open)
    def test_save_data(self, mock_file):
        from storage import save_data, get_data
        mock_data = {"abc123": "https://example.com"}
        
        # Mock the return of get_data() to simulate an existing JSON file
        with patch('storage.get_data', return_value=mock_data):
            result = save_data("https://newsite.com", "def456")
        
        # Test if save_data modifies the dictionary and writes it back
        self.assertTrue(result)
        
        # Capture all the write calls
        handle = mock_file()
        written_content = ''.join(call.args[0] for call in handle.write.call_args_list)
        
        # Expected JSON content
        expected_data = json.dumps({"abc123": "https://example.com", "def456": "https://newsite.com"})
        
        # Ensure that the entire content written matches the expected data
        self.assertEqual(written_content, expected_data)

    # Test for get_original_url function when hash exists
    @patch("builtins.open", new_callable=mock_open, read_data='{"abc123": "https://example.com"}')
    def test_get_original_url_exists(self, mock_file):
        from storage import get_original_url
        result = get_original_url("abc123")
        self.assertEqual(result, "https://example.com")
        mock_file.assert_called_once_with('data.json', 'r')

    # Test for get_original_url function when hash does not exist
    @patch("builtins.open", new_callable=mock_open, read_data='{"abc123": "https://example.com"}')
    def test_get_original_url_not_exists(self, mock_file):
        from storage import get_original_url
        result = get_original_url("def456")
        self.assertIsNone(result)
        mock_file.assert_called_once_with('data.json', 'r')

if __name__ == '__main__':
    unittest.main()
