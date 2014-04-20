from flask import Flask, jsonify, make_response
from flask_cors import cross_origin
from tractatus import Tractatus


app = Flask(__name__)

# Set the correct origin
app.config['CORS_ORIGINS'] = ['http://wittgenste.in']

@app.route("/")
def hello():
    return "Visit /random for a random passage from the Tractatus."

@app.route("/random")
@cross_origin() # allow all origins all methods.
def random(methods = ['GET']):
    # Build the Tractatus and get a random section
    # print "Build tractatus"
    tractatus = Tractatus()
    # print "Then get the book"
    book = tractatus.get_book()
    # print "then get a section"
    section = book.get_random_section()
    # print "Then return json"
    # Print out the JSON
    return section.to_json()

@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify( { 'error': 'Error 404: What we cannot speak about we must pass over in silence.' } ), 404)

@app.errorhandler(500)
def server_error(error):
    return make_response(jsonify( { 'error': 'Error 500: Something went wrong behind the scenes...' } ), 500)

if __name__ == "__main__":
    app.run()