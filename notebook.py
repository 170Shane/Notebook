import datetime

# Store the next available id for all new notes
last_id = 0


class Note:
    """Represents a note in the notebook. Match against a string in searches and store tags for each note"""

    def __init__(self, memo, tags=''):
        """Initialise a note with memo and optional space-separated tags. Automatically set the note's creation date
        and a unique ID"""

        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """Determine if this note matches the filter text. Return True if it matches, False otherwise.
        Search in case-sensitive and matches both text and tags"""
        return filter in self.memo or filter in self.tags


# n1 = Note('hello first')
# n2 = Note('hello again')
#
# print(n1.id)
# print(n2.id)
# print(n1.match('hel'))
# print(n2.match('goodbye'))
class Notebook:
    """Represent a collection of notes that can be tagged, modified and searched"""

    def __init__(self):
        """Initialises a notebook with an empty list"""
        self.notes = []

    def new_note(self, memo, tags=''):
        """Create a new note and add it to the list"""
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        """Find the note with the given ID and change it's value to the given value"""
        self._find_note(note_id).memo = memo

    def modify_tags(self, note_id, tags):
        """Find the note with the given ID and change it's tags to the given value"""
        for note in self.notes:
            if note.id == note_id:
                self._find_note(note_id).tags = tags
                break

    def search(self, filter):
        """Find all notes that match the given filter string"""
        return [note for note in self.notes if note.match(filter)]

    def _find_note(self, note_id):
        """Locate the note with the given ID"""
        for note in self.notes:
            if note.id == note_id:
                return note
            return None


def main():
    n = Notebook()
    n.new_note('hello first')
    n.new_note('hello again')
    print(n.notes[0].id)
    print(n.notes[1].id)
    print(n.notes[0].memo)
    print(n.notes[1].memo)
    n.modify_memo(1, 'This value should now be updated')
    print(n.notes[0].memo)
    print(n.notes[1].memo)
    print(n.search('z'))


if __name__ == '__main__':
    main()
