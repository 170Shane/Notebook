from notebook import Note, Notebook

note_1 = Note('This is my first note', '1st, initial, debut, main')
note_2 = Note('This is my second note', '2nd, second')

for tag in note_1.tags.split(', '):
    print(tag, note_1.id)

    print(note_2.id)


print(note_1.match('1'))

notebook_1 = Notebook()
notebook_1.new_note('This is my third note', '3rd, third')

for note in notebook_1.notes:
    print(note.id)
