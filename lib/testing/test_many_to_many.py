import unittest
from many_to_many import Author, Book, Contract

class TestBookAuthorContract(unittest.TestCase):

    def setUp(self):
        self.author = Author("J.K. Rowling")
        self.book = Book("Harry Potter")
        self.contract = self.author.sign_contract(self.book, "2023-01-01", 15)

    def test_author_creation(self):
        self.assertEqual(self.author.name, "J.K. Rowling")
        self.assertIn(self.author, Author.all_authors)

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Harry Potter")
        self.assertIn(self.book, Book.all_books)

    def test_sign_contract(self):
        self.assertEqual(self.contract.author, self.author)
        self.assertEqual(self.contract.book, self.book)
        self.assertEqual(self.contract.date, "2023-01-01")
        self.assertEqual(self.contract.royalties, 15)
        self.assertIn(self.contract, Contract.all_contracts)

    def test_author_contracts(self):
        self.assertEqual(self.author.contracts(), [self.contract])

    def test_author_books(self):
        self.assertEqual(self.author.books(), [self.book])

    def test_total_royalties(self):
        self.assertEqual(self.author.total_royalties(), 15)

    def test_contracts_by_date(self):
        contracts = Contract.contracts_by_date("2023-01-01")
        self.assertIn(self.contract, contracts)

if __name__ == "__main__":
    unittest.main()
