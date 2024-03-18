from main import bookrepo as repo

# Domain methods
def getNextId():
	next_id = repo.ids['next_id'] + 1
	repo.ids['next_id'] = next_id
	return next_id

def getBookById(id):
	return repo.books[int(id)]

def getSpecificBooks(paramName, paramValue):
	results = []
	for book in repo.books.values():
		if paramValue in book[paramName]:
			results.append(book)
	return results

def createBook(title, author, series, year, rating):
	id = getNextId()
	if title is not None and author is not None:
		new_book = {'id':id,'title':title,'author':author,'series':series,'year_published':year,'rating':rating}
		repo.books[id] = new_book
		return new_book
	else:
		raise ValueError('Title or author must not be null')

def updateBook(id, title, author, series, year, rating):
	id = int(id)
	book_to_update = getBookById(id)
	if title is not None:
		book_to_update['title'] = title
	if author is not None:
		book_to_update['author'] = author
	if series is not None:
		book_to_update['series'] = series

	book_to_update['year_published'] = int(year)

	if rating is not None:
		book_to_update['rating'] = rating

	repo.books[id] = book_to_update

def deleteBook(id):
	del repo.books[int(id)]
