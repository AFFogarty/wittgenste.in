from flask import Flask
from book import Book
from tractatus import Tractatus

app = Flask(__name__)

@app.route("/")
def hello():
    return "Visit /random for a random passage from the Tractatus."

@app.route("/random")
def random():
    # Build the Tractatus and get a random section
    tractatus = Tractatus()
    book = tractatus.get_book()
    section = book.get_random_section()

    # Print out the JSON
    return section.to_json()

@app.errorhandler(404)
def page_not_found(error):
    return 'Error 404: What we cannot speak about we must pass over in silence.', 404

@app.errorhandler(500)
def server_error(error):
    return 'Error 500: Something went wrong behind the scenes...', 500

if __name__ == "__main__":
    app.run()