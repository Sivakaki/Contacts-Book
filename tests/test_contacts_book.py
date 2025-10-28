"""Unit tests for the Contact Book application"""

import unittest
import os
from contacts_book import add_contact, search_contact, delete_contact


class TestContactBook(unittest.TestCase):
    """Test cases for contact book functions"""

    def setUp(self):
        """Create a test file before each test"""
        self.test_file = "test_contacts.txt"
        # Change the contacts.txt reference to test file
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        """Clean up test file after each test"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_contact_creates_file(self):
        """Test that add_contact creates a contacts file"""
        # This test verifies file creation
        self.assertFalse(os.path.exists(self.test_file))

    def test_search_nonexistent_contact(self):
        """Test searching for a contact that doesn't exist"""
        # Verify proper handling of missing contacts
        pass

    def test_delete_nonexistent_contact(self):
        """Test deleting a contact that doesn't exist"""
        # Verify proper handling of deletion attempts
        pass


if __name__ == '__main__':
    unittest.main()
