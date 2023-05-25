from typing import List
from models.note import Note
from presenters.model import Model
from presenters.view import View
from presenters.view_observer import View_observer


class Presenter(View_observer):
    notes: List[Note] = []

    def __init__(self, model: Model, view: View) -> None:
        super().__init__()
        self.model = model
        self.view = view
        self.view.observer = self

    def start(self):
        self.notes = self.model.load_data()
        self.view.show_main_menu()

    def on_show_all_notes(self):
        self.view.show_notes(self.notes)

    def on_add_note(self):
        titleAndBody = self.view.show_adding()
        self.model.add_note(
            notes=self.notes, title=titleAndBody[0], body=titleAndBody[1])

    def on_edit_note(self):
        pass

    def on_delete_note(self):
        self.model.delete_note(
            notes=self.notes, index=self.view.show_deleting(self.notes))
