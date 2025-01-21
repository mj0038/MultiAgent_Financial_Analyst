import unittest
from crew.crew_manager import create_crew

class TestApp(unittest.TestCase):
    def test_crew_creation(self):
        file_path = create_crew("AAPL", "OpenAI GPT-4o Mini")
        self.assertTrue(file_path.endswith("AAPL_analysis.txt"))

if __name__ == "__main__":
    unittest.main()
