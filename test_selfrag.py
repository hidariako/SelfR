# test_selfrag.py
"""
Tests for SelfRAG module.
"""

import unittest
from selfrag import SelfRAG

class TestSelfRAG(unittest.TestCase):
    """Test cases for SelfRAG class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SelfRAG()
        self.assertIsInstance(instance, SelfRAG)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SelfRAG()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
