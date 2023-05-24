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