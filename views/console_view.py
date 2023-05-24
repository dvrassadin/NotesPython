from typing import List
from models.note import Note
from presenters.view import View


class Console_view(View):
    def show_main_menu(self):
        while True:
            action = input('''Enter the number of action:
1 — Show all notes
0 — Exit
>>> ''')
            if action == "0":
                break
            elif action == "1":
                self.observer.show_all_notes()
            else:
                print("The number is incorrect\n")

    def show_all_notes(self, notes: List[Note]):
        for note in notes:
            print(note)
