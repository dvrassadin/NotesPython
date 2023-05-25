from abc import ABC, abstractmethod
from typing import List

from models.note import Note


class Model(ABC):
    @abstractmethod
    def load_data(self) -> List[Note]:
        pass

    @abstractmethod
    def save_data(self, notes: List[Note]):
        pass

    @abstractmethod
    def add_note(self, notes: List[Note], title: str, body: str):
        pass

    @abstractmethod
    def delete_note(self, notes: List[Note], index):
        pass

    @abstractmethod
    def edit_note(self, notes: List[Note], index: int, isTitle: bool, newText: str):
        pass
