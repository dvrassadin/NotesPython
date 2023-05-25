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
5 - Find by date
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
            elif action == "5":
                self.observer.on_find_by_date()
            else:
                print("The number is incorrect.")

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

    def show_short_notes(self, notes: List[Note]):
        if notes:
            for note in notes:
                print(f"{note.id}\t{note.date} {note.title}")
        else:
            print("There are no notes.")

    def show_deleting(self, notes: List[Note]) -> int:
        if notes:
            while True:
                index = input(
                    "Enter the number of note you want to delete or 0 to cancel: ")
                if index.isdigit():
                    intIndex = int(index)
                    if intIndex == 0:
                        return
                    elif intIndex > len(notes) or intIndex < 1:
                        print("This is the wrong number, enter another number: ")
                    else:
                        return intIndex - 1

    def show_editing(self, notes: List[Note]):
        realIndex: int
        isTitle: bool

        while True:
            index = input(
                "Enter the number of note you want to edit or 0 to cancel: ")
            if index.isdigit():
                intIndex = int(index)
                if intIndex == 0:
                    return
                elif intIndex > len(notes) or intIndex < 1:
                    print("This is the wrong number, enter another number: ")
                else:
                    realIndex = intIndex - 1
                    break

        print(notes[realIndex])

        while True:
            attribute = input('''Enter what you want to change:
1 — Title
2 — Text
0 — Cancel
>>> ''')
            if attribute == "0":
                return
            elif attribute == "1":
                isTitle = True
                break
            elif attribute == "2":
                isTitle = False
                break
            else:
                print("This is the wrong number, enter another number: ")

        newText = input("Enter new text:\n")

        return (realIndex, isTitle, newText)


    def show_date_entering(self) -> str:
        return input("Enter the date like dd.mm.yyyy: ")


    def show_date_format_error(self):
        print("The date format is incorrect.\n")
