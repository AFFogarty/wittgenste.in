from flask import Flask

from tractatus import Tractatus


app = Flask(__name__)

@app.route("/")
def hello():
    return "Visit /random for a random passage from the Tractatus."

@app.route("/random")
def random():
    # Build the Tractatus and get a random section
    tractatus = None
    book = None
    section = None

    try:
        tractatus = Tractatus()
    except:
        return "Tractatus initialization error."
    try:
        book = tractatus.get_book()
    except:
        return "Get book error."
    try:
        section = book.get_random_section()
    except:
        return "Get section error!"

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