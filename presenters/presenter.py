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

    def show_all_notes(self):
        self.view.show_all_notes(self.notes)
