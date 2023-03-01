from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Author import Author
# Models
from models.AuthorModel import AuthorModel

main = Blueprint('authors_blueprint', __name__)

@main.route('/')
def get_authors():
    try:
        authors = AuthorModel.get_authors()
        return jsonify(authors)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_author(id):
    try:
        author = AuthorModel.get_author(id)
        if author != None:
            return jsonify(author)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_author():
    try:
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        id = uuid.uuid4()
        id = int(id)
        author = Author(id, first_name, last_name)

        affected_rows = AuthorModel.add_author(author)

        if affected_rows == 1:
            return jsonify(author.id)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_author(id):
    id=int(id)
    try:
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        author = Author(id, first_name, last_name)

        affected_rows = AuthorModel.update_author(author)

        if affected_rows == 1:
            return jsonify(author.id)
        else:
            return jsonify({'message': "No author updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_author(id):
    id=int(id)
    try:
        author = Author(id)

        affected_rows = AuthorModel.delete_author(author)

        if affected_rows == 1:
            return jsonify(author.id)
        else:
            return jsonify({'message': "No author deleted"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500