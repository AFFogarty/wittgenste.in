from book import Book

class Tractatus:
    # This is the book
    tractatus = None

    def __init__(self):
        """ Construct the Tractatus """

        # Build the Book object
        self.tractatus = Book()
        print "Tractatus initialized"

        # Get the tractatus from text
        all_text = open('res/tractatus.txt', 'r')
        output = all_text.readlines()

        print "text file downloaded"

        print len(output)

        # Read the file line by line into self.tractatus
        # The actual content only begins at line 30 until the end
        for i in range(30, len(output)):
            complete_string = str(output[i])

            # We need to separate the index and the text
            split_string = complete_string.partition(" ")
            index = split_string[0]
            text = split_string[2].rstrip("\n")

            # Load them in
            self.tractatus.add_section(index, text)

        print "loop complete"
        print self.tractatus

    def get_book(self):
        return self.tractatus





