import unittest
from Extractor import filesCopier, notebookExtractor

class TestUtils(unittest.TestCase):
    def test_filesCopier_success(self):
        actual = filesCopier(['main1.py', 'main2.py'], sourceDir="./tests/sources", outputDir="./tests/outputs")
        
        self.assertEqual(actual, None)

    def test_filesCopier_failed_file_not_found(self):
        with self.assertRaises(FileNotFoundError) as context:
            filesCopier(['main1.py', 'main2.py'], sourceDir="./tests/source", outputDir="./tests/outputs")

    def test_notebookExtractor_success(self):
        actual = notebookExtractor(['note1.ipynb', 'note2.ipynb'], sourceDir="./tests/sources", outputDir="./tests/outputs")
        
        self.assertEqual(actual, None)

    def test_notebookExtractor_failed(self):
        with self.assertRaises(Exception) as context:
            notebookExtractor(['main1.py', 'main2.py'], sourceDir="./tests/source", outputDir="./tests/outputs")

if __name__ == "__main__":
    unittest.main()