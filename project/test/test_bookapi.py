import unittest

from main import bookdomain as bookapi

class BasicTests(unittest.TestCase):

	def test_nothing(self):
		self.assertTrue(1==1, "I don't always test my code; but when I do, I do it in PRODUCTION.")

	def test_getNextId(self):
		id_1 = bookapi.getNextId()
		id_2 = bookapi.getNextId()

		self.assertEqual(id_1 + 1, id_2, "IDs are not incremented correctly.")

	def test_getBookById(self):
		book = bookapi.getBookById(0)

		self.assertEqual('James Barclay', book['author'])
		self.assertEqual('Dawnthief', book['title'])

	def test_createBook(self):
		id = bookapi.getNextId()
		bookapi.createBook('Noonshade', 'James Barclay', 'The chronicles of the raven', 2004, 'amazing')
		book = bookapi.getBookById(id + 1)

		self.assertEqual('James Barclay', book['author'])
		self.assertEqual('Noonshade', book['title'])
		self.assertEqual('The chronicles of the raven', book['series'])
		self.assertEqual(2004, book['year_published'])
		self.assertEqual('amazing', book['rating'])

	def test_updateBook(self):
		id = bookapi.getNextId()
		bookapi.createBook('Noonshade', 'James Barclay', 'The chronicles of the raven', 2004, 'amazing')
		bookapi.updateBook(id + 1, 'Noonshade 2', 'Super James Barclay', 'The chronicles of the Raven', 2003, 'reallyamazing')
		book = bookapi.getBookById(id + 1)

		self.assertEqual('Super James Barclay', book['author'])
		self.assertEqual('Noonshade 2', book['title'])
		self.assertEqual('The chronicles of the Raven', book['series'])
		self.assertEqual(2003, book['year_published'])
		self.assertEqual('reallyamazing', book['rating'])

	def test_deleteBook(self):
		id = bookapi.getNextId()
		bookapi.createBook('Noonshade', 'James Barclay', 'The chronicles of the raven', 2004, 'amazing')
		bookapi.deleteBook(id + 1)

		self.assertRaises(KeyError, bookapi.getBookById, id + 1)


if __name__ == '__main__':
	unittest.main()
