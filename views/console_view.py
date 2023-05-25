from typing import List
from models.note import Note
from presenters.view import View


class Console_view(View):
    def show_main_menu(self):
        while True:
            action = input('''Enter the number of action:
1 — Show all notes
2 — Add a note
3 - Edit a note
4 - Delete a note
0 — Exit
>>> ''')
            if action == "0":
                break
            elif action == "1":
                self.observer.on_show_all_notes()
            elif action == "2":
                self.observer.on_add_note()
            elif action == "3":
                self.observer.on_edit_note()
            elif action == "4":
                self.observer.on_delete_note()
            else:
                print("The number is incorrect\n")

    def show_notes(self, notes: List[Note]):
        if notes:
            for note in notes:
                print(note)
        else:
            print("There are no notes.")

    def show_adding(self):
        title = input("Enter the title:\n")
        body = input("Enter text of the note:\n")
        return (title, body)

    def show_deleting(self, notes: List[Note]) -> int:
        if notes:
            for note in notes:
                print(f"{note.id}\t{note.date} {note.title}")
            while True:
                index = input(
                    "Enter the number of note you want to delete or 0 to cancel: ")
                if index.isdigit():
                    intIndex = int(index)
                    if intIndex == 0:
                        break
                    elif intIndex > len(notes) or intIndex < 1:
                        print("This is the wrong number, enter another number: ")
                    else:
                        return intIndex - 1

        else:
            print("There are no notes.")
