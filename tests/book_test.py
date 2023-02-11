import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("The Lord of the Rings", "T R R Tolkien", "Fantasy")

    def test_has_title(self):
        expect = "The Lord of the Rings"
        actual = self.book.title
        self.assertEqual(expect, actual)

    def test_has_author(self):
        expected = "T R R Tolkien"
        actual = self.book.author
        self.assertEqual(expected, actual)

    def test_has_genre(self):
        expected = "Fantasy"
        actual = self.book.genre
        self.assertEqual(expected, actual)