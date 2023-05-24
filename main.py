from datetime import datetime
from models.note import Note
from models.note_model import Note_model
from presenters.model import Model


if __name__ == "__main__":
    model: Model = Note_model()

    notes = model.load_data()

    notes.append(Note(3, date=datetime.now(), title="Third!!!",
                 body="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."))

    model.save_data(notes)

    for note in notes:
        print(note)
