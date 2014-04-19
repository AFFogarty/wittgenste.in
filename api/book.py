import random
from flask import json


class Book:
    sections = []

    def __init__(self):
        """ Build the book """

        for i in range(13):
            self.sections.append(random.randint(0, 10000000000000000000000))

    def add_section(self, index, text):
        """ Add a section to the book """
        passage = Passage(index, text)
        self.sections.append(passage)

    def get_all_sections(self):
        """ Get all sections """
        return self.sections

    def get_section(self, i):
        # Make sure we aren't getting an illegal id
        if i < 0 or i > len(self.sections):
            return None

        # The index is good, so return it
        return self.sections[i]

    def get_random_section(self):
        """ Get a random section from the book. """
        return self.sections[random.randint(0, len(self.sections))]


class Passage:
    index = None
    text = None

    def __init__(self, index, text):
        """ Set up the passage """
        self.index = index
        self.text = text

    def __str__(self):
        return "Book[index : " + self.index + ", text : " + self.text + "] "

    def to_json(self):
        return json.jsonify(index=self.index, text=self.text)