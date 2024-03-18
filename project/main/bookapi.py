from flask import *
import json
import sys
from main import bookrepo as repo
from main import bookdomain as dom

app = Flask("BookApi")

# API methods
@app.route("/")
def hello():
	return jsonify({'message':'A simple API with books'})

@app.route("/books")
def getAll():
	rating = request.args.get('rating')
	if rating is not None:
		return jsonify(dom.getSpecificBooks('rating', rating))

	title = request.args.get('title')
	if title is not None:
		return jsonify(dom.getSpecificBooks('title', title))

	return jsonify(repo.books), 200

@app.route("/books", methods=['POST'])
def create():
	data = request.json
	title = data.get('title')
	author = data.get('author')
	series = data.get('series')
	year = data.get('year_published')
	rating = data.get('rating')
	try:
		new_book = dom.createBook(title, author, series, year, rating)
		return jsonify(new_book), 201
	except ValueError as ve:
		return jsonify({'message':'Title and author must be provided to create a valid book'}), 422

@app.route("/books/<id>")
def getOne(id):
	try:
		results = dom.getBookById(int(id))
		return jsonify(results), 200
	except ValueError as te:
		return jsonify({'message': 'ID must be a valid number'}), 422
	except KeyError as ke:
		return jsonify({'message': 'Specified ID does not exist'}), 404

@app.route("/books/<id>", methods=['PUT'])
def update(id):
	data = request.json
	title = data.get('title')
	author = data.get('author')
	series = data.get('series')
	year = data.get('year_published')
	rating = data.get('rating')
	try:
		dom.updateBook(id, title, author, series, year, rating)
		return ('', 204)
	except ValueError as te:
		return jsonify({'message': 'ID must be a valid number'}), 400
	except KeyError as ke:
		return jsonify({'message': 'Specified ID does not exist'}), 404

@app.route("/books/<id>", methods=['DELETE'])
def delete(id):
	try:
		dom.deleteBook(id)
		return ('', 204)
	except ValueError as te:
		return jsonify({'message': 'ID must be a valid number'}), 400
	except KeyError as ke:
		return jsonify({'message': 'Specified ID does not exist'}), 404

if __name__ == '__main__':
	args = sys.argv[1:]
	app_port = args[0]
	app.run(debug = True, host="0.0.0.0", port=app_port)
