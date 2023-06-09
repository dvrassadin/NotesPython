from abc import ABC, abstractmethod
from typing import List
from models.note import Note
from presenters.view_observer import View_observer


class View(ABC):
    observer: View_observer

    @abstractmethod
    def show_main_menu(self):
        pass

    @abstractmethod
    def show_notes(self, notes: List[Note]):
        pass

    @abstractmethod
    def show_short_notes(self, notes: List[Note]):
        pass

    @abstractmethod
    def show_adding(self):
        pass

    @abstractmethod
    def show_deleting(self, notes: List[Note]) -> int:
        pass

    @abstractmethod
    def show_editing(self, notes: List[Note]):
        pass

    @abstractmethod
    def show_date_entering(self) -> str:
        pass

    @abstractmethod
    def show_date_format_error(self):
        pass
