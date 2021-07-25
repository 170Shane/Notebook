import sys
from notebook import Notebook


class Menu:
    """Display a menu and respond to choices when run"""

    def __init__(self):
        self.notebook = Notebook()  # initialise a new Notebook
        self.choices = {
            "1": self.show_notes,
            # "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def display_menu(self):
        print("""
        Notebook Menu
        
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """)

    def run(self):
        """Display the menu and respond to choice"""

        while True:
            self.display_menu()
            choice = input("Please enter an option: ")
            action = self.choices.get(choice)  # set 'action' = dictionary choice i.e. name of function
            if action:
                action()  # execute the chosen function
            else:
                print(f"{choice} is not a valid choice")  # else display friendly message to user

    def show_notes(self, notes=None):
        if not notes:  # if we are not being passed a list of notes that have been filtered for a match
            notes = self.notebook.notes  # display all notes in the Notebook
        for note in notes:  # loop through the notes collection which will be either all notes or notes that
            # have matched the search pattern
            print(f"{note.id}: {note.tags}\n{note.memo}")  # print out the notes and some additional details

    #
    # def search_notes(self):
    #     filter = input("Search for: ")
    #     notes = self.notebook.search(filter)
    #     self.show_notes(notes)
    #
    def add_note(self):
        memo = input("Enter a memo: ")
        tags = input("Hit me with some tags: ")
        self.notebook.new_note(memo, tags)
        print("Your note has been added")

    def modify_note(self):
        try:
            id = int(input("Enter a note ID: "))
            # do we have a valid ID?
            if self.notebook._find_note(id) is not None:
                memo = input("Enter a memo: ")
                tags = input("Enter tags: ")
                if memo:
                    self.notebook.modify_memo(id, memo)
                if tags:
                    self.notebook.modify_tags(id, tags)
        except ValueError:
            print('Incorrect Note Value entered. Please try again')
        except Exception as e:
            print(e)

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
